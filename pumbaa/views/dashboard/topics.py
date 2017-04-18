

import json

from pumbaa import models
from pumbaa import forms

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

module = Blueprint('dashboard.topics', __name__)

from pumbaa.acl import dashboard_permission

# @view_config(route_name='manager.topics.index', 
#              permission='member',
#              renderer='/manager/topics/index.mako')
@module.route('/')
@dashboard_permission.require()
def index():
    user = current_user._get_current_object()
    topics = models.Topic.objects(status__ne='delete',
            author=user).all()
    return render_template('/dashboard/topics/index.jinja2',
            topics=topics
            )
    
# @view_config(route_name='manager.topics.problem', 
#              permission='topic',
#              renderer='/manager/topics/problem.mako')
def problem():
    topics = models.Topic.objects(status__nin=['delete', 'publish']).all()
    return dict(
                topics=topics
                )

# @view_config(route_name='manager.topics.change_status', 
#              permission='topic', )
def change_status():
    topic_id = request.matchdict.get('topic_id')
    status = request.matchdict.get('status')
    
    default_status = ['publish', 'suspend', 'delete']
    if status not in default_status:
        return Response('This status not allow', status='500')
    
    topic = models.Topic.objects.with_id(topic_id)
    if topic is None:
        return Response('Not Found, topic title:%s'%topic_id, status='404 Not Found')
    
    topic.status = status
    topic.save()
    
    if status == 'delete':
        return HTTPFound(location=request.route_path('manager.topics.problem'))
    
    return HTTPFound(location=request.route_path('forums.topics.index'))

# @view_config(route_name='forums.topics.compose', 
#              permission='member',
#              renderer='/forums/topics/compose.mako')
@module.route('/compose')
@dashboard_permission.require()
def compose():
    # form = forms.topics.Topic(request.form)
    
    # if len(request.form) > 0 and form.validate():
    #     title = form.data.get('title')
    #     description = form.data.get('description')
    #     tags = form.data.get('tags')
    #     if '' in tags:
    #         tags.remove('')
    form = forms.topics.Topic()
    
    if form.validate_on_submit():
        title = form.data.get('title')
        description = form.data.get('description')
        tags = form.data.get('tags')
        if '' in tags:
            tags.remove('')
              
    else:
        tags = models.Topic.objects().distinct('tags')
        tags.extend(models.Forum.objects().distinct('tags'))
        
        ## set default tags for roles
        role = [role.name for role in current_user.roles]
        if "lecturer" in role:
            default_tags = "ปรกาศจากทางภาควิชา"
        elif "staff" in role:
            default_tags = "ประกาศจากทางภาควิชา"
        elif "member" in role:
            default_tags = "พูกคุยทั่วไป"
        else:
            default_tags = ""
        ## end set

        return render_template('/dashboard/topics/compose.jinja2',
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


