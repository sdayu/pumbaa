import json

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pumbaa import models
from pumbaa import forms

@view_config(route_name='manager.events.index', 
             permission='member',
             renderer='/manager/events/index.mako')
def index(request):
    events = models.Event.objects(status__ne='delete', author=request.user)
    return dict(
                events=events
                )

@view_config(route_name='manager.events.create', 
             permission='member',
             renderer='/manager/events/event.mako')
def create(request):
    form = forms.events.Event(request.POST)

    if len(request.POST) == 0 or not form.validate():
        if len(request.POST) == 0:
            form.tags.data = ['Event']
        tags = models.Topic.objects().distinct('tags')
        return dict(form=form, tags=json.dumps(tags))
    
    topic = models.Topic(**form.data)
    event = models.Event(**form.data)
    topic.status = 'publish'
    topic.author = request.user
    topic.type = 'event'
    topic.published_date = topic.updated_date
    topic.ip_address = request.environ.get('REMOTE_ADDR', '0.0.0.0')
    if not event.event_type in topic.tags:
        topic.tags.append(event.event_type)
    if not 'Event' in topic.tags:
        topic.tags.append('Event')
    topic.save()
    
    event.topic = topic
    event.author = request.user
    event.ip_address = request.environ['REMOTE_ADDR']
    event.status = 'publish'
    
    event.save()
    return HTTPFound(location=request.route_path('manager.events.index'))

@view_config(route_name='manager.events.edit', 
             permission='member',
             renderer='/manager/events/event.mako')
def edit(request):
    event_id = request.matchdict.get('event_id')
    form = forms.events.Event(request.POST)
    event = models.Event.objects(id=event_id, author=request.user).first()
    
    if len(request.POST) == 0 or not form.validate():
        if len(request.POST) == 0:
            event.title = event.topic.title
            event.description = event.topic.description
            event.tags = event.topic.tags
            form = forms.events.Event(obj=event)
        tags = models.Topic.objects().distinct('tags')
        return dict(form=form, tags=json.dumps(tags))
  
    form.populate_obj(event)
    event.topic.title = form.data['title']
    event.topic.description = form.data['description']
    event.topic.tags = form.data['tags']
    
    if not event.event_type in event.topic.tags:
        event.topic.tags.append(event.event_type)
    
    if not 'Event' in event.topic.tags:
        event.topic.tags.append('Event')
        
    event.topic.save()
    event.save()
    
    return HTTPFound(location=request.route_path('manager.events.index'))


@view_config(route_name='manager.events.delete',
             permission='member')
def delete(request):
    event_id = request.matchdict.get('event_id')
    event = models.Event.objects.with_id(event_id)
    event.status = 'delete'
    event.topic.status = 'delete'
    event.save()
    event.topic.save()
    return HTTPFound(location=request.route_path('manager.events.index'))
