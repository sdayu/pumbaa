'''
Created on Oct 18, 2013

@author: boatkrap
'''
from flask import Blueprint, render_template, request, redirect, make_response, current_app, url_for
from authomatic.adapters import WerkzeugAdapter

from flask_login import login_required, current_user, login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity

from pumbaa import models, forms
import json
import math

module = Blueprint('forums.topics', __name__)

# @view_config(route_name='forums.topics.index', 
#              renderer='/forums/topics/index.mako')
@module.route('/')
def index():
    page = int(request.args.get('page', 1))
    topics_per_page = 15
    
    topic_count = models.Topic.objects(status='publish').count()
    pages = math.ceil(topic_count/topics_per_page)
    
    page = page if page > 0 else 1
    page = page if page <= pages else pages
    
    topics = models.Topic.objects(status='publish').order_by('-published_date').skip((page-1)*topics_per_page).limit(topics_per_page).all()
    return render_template('/forums/topics/index.jinja2',
                topics=topics,
                pages=pages,
                page=page
                )

# @view_config(route_name='forums.topics.compose', 
#              permission='member',
#              renderer='/forums/topics/compose.mako')
def compose(request):
    form = forms.topics.Topic(request.POST)
    
    if len(request.POST) > 0 and form.validate():
        title = form.data.get('title')
        description = form.data.get('description')
        tags = form.data.get('tags')
        if '' in tags:
            tags.remove('')
            
    else:
        tags = models.Topic.objects().distinct('tags')
        tags.extend(models.Forum.objects().distinct('tags'))
        
        ## set default tags for roles
        role = [role.name for role in request.user.roles]
        if "lecturer" in role:
            default_tags = "ปรกาศจากทางภาควิชา"
        elif "staff" in role:
            default_tags = "ประกาศจากทางภาควิชา"
        elif "member" in role:
            default_tags = "พูกคุยทั่วไป"
        else:
            default_tags = ""
        ## end set

        return dict(
                    tags = json.dumps(tags),
                    form = form,
                    default_tags = default_tags
                    )
    
    topic = models.Topic(title=title, description=description, tags=tags)
    topic.author = request.user
    topic.published_date = topic.updated_date
    topic.status = 'publish'
    topic.ip_address = request.environ.get('REMOTE_ADDR', '0.0.0.0')
    
    history = models.TopicHistory(author=request.user, 
                                  changed_date=topic.updated_date,
                                  title=topic.title, 
                                  description=topic.description,
                                  tags=topic.tags)
    topic.histories.append(history)
    topic.save()
    topic.reload()
    
    #auto post to fb
    from pumbaa.libs import auto_post_fb as autopost_fb
    post_to_fb = autopost_fb.AutoPostFacebook(request)
    if post_to_fb.enable:

        forum_tags = []
        for fid in post_to_fb.forum_id:
            forum = models.Forum.objects.with_id(fid)
            forum_tags.extend(forum.tags)

        if any([tag in forum_tags for tag in tags]):
            url = request.route_url('forums.topics.view', title=title, topic_id=topic.id)
            fb_status = title + "\n" + description +"\n"+url

            post_to_fb.post_to_fb_group(fb_status)

    return HTTPFound(location=request.route_path('forums.topics.view', title=title, topic_id=topic.id))

# @view_config(route_name='forums.topics.view', 
#              renderer='/forums/topics/view.mako')
@module.route('/<topic_id>/<title>')
def view(topic_id, title):
    
    topic = models.Topic.objects(id=topic_id, status='publish').first()
    
    if topic is None:
        return Response('Not Found, topic title:%s'%title, status='404 Not Found')
        
    return render_template('/forums/topics/view.jinja2',
            topic=topic
            )
