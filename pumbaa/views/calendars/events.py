'''
Created on May 23, 2014

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pumbaa import models

@view_config(route_name='calendars.events.index', renderer='/calendars/events/index.mako')
def index(request):
    tags = models.Topic.objects(status='publish', type='event').distinct('tags')
    return dict(tags=tags)

@view_config(route_name='calendars.events.view', renderer='/calendars/events/view.mako')
def view(request):
    event_id = request.matchdict.get('event_id')
    event = models.Event.objects(id=event_id, status='publish').first()
    
    if not event:
        return Response('Event not Found')
    
    if event.topic.status != 'publish':
        return HTTPFound('Event not publish')
    return dict(event=event)

@view_config(route_name='calendars.events.list_by_tags', renderer='/calendars/events/list_events.mako')
def list_by_tags(request):
    tname = request.matchdict.get('name')
    topics = models.Topic.objects(tags__icontains=tname, status='publish')
    events = models.Event.objects(topic__in=topics, status='publish')

    return dict(events=events, tag=tname)