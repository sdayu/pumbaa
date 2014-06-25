'''
Created on Oct 18, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pumbaa.libs import mailer
from pumbaa import models, forms
import json
import math

@view_config(route_name='forums.topics.index', 
             renderer='/forums/topics/index.mako')
def index(request):
    page = int(request.GET.get('page', 1))
    topics_per_page = 15
    
    topic_count = models.Topic.objects(status='publish').count()
    pages = math.ceil(topic_count/topics_per_page)
    
    page = page if page > 0 else 1
    page = page if page <= pages else pages
    
    topics = models.Topic.objects(status='publish').order_by('-published_date').skip((page-1)*topics_per_page).limit(topics_per_page).all()
    return dict(
                topics=topics,
                pages=pages,
                page=page
                )

@view_config(route_name='forums.topics.compose', 
             permission='member',
             renderer='/forums/topics/compose.mako')
def compose(request):
    form = forms.topics.Topic(request.POST)
    
    if len(request.POST) > 0 and form.validate():
        title = form.data.get('title')
        description = form.data.get('description')
        tags = [tag.strip() for tag in form.data.get('tags').split(',')]
        if '' in tags:
            tags.remove('')
            
    else:
        tags = models.Topic.objects().distinct('tags')
        tags.extend(models.Forum.objects().distinct('tags'))
        
        return dict(
                    tags = json.dumps(tags),
                    form = form
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
    mail = mailer.Mailer()
    if mail.enable:

        forum_tags = []
        for fid in mail.forum_id:
            forum = models.Forum.objects.with_id(fid)
            forum_tags.extend(forum.tags)

        if any([tag in forum_tags for tag in tags]):
            url = request.route_url('forums.topics.view', title=title, topic_id=topic.id)
            fb_status = title + "\n" + description +"\n"+url

            from pyramid_mailer import get_mailer
            pymailer = get_mailer(request)

            from pyramid_mailer.message import Message
            print(mail.sender)
            print(mail.recipient)
            message = Message(subject=None,
                              sender=mail.sender,
                              recipients=[mail.recipient],
                              body=fb_status)
            #pymailer.send(message)
            pymailer.send_immediately(message, fail_silently=False)

            #mail.post_to_fb_group(fb_status)

    return HTTPFound(location=request.route_path('forums.topics.view', title=title, topic_id=topic.id))

@view_config(route_name='forums.topics.view', 
             renderer='/forums/topics/view.mako')
def view(request):
    topic_id = request.matchdict.get('topic_id')
    title = request.matchdict.get('title')
    
    topic = models.Topic.objects(id=topic_id, status='publish').first()
    
    if topic is None:
        return Response('Not Found, topic title:%s'%title, status='404 Not Found')
        
    return dict(
                topic=topic
                )
