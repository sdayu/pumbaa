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
    events = models.Event.objects(status__ne='delete')
    return dict(
                events=events
                )

@view_config(route_name='manager.events.add', 
             permission='member',
             renderer='/manager/events/event.mako')
def add(request):
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
    topic.save()
    
    event.topic = topic
    event.author = request.user
    event.ip_address = request.environ['REMOTE_ADDR']
    event.status = 'publish'
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
