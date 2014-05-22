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
    topics = []
    return dict(
                topics=topics
                )

@view_config(route_name='manager.events.add', 
             permission='member',
             renderer='/manager/events/event.mako')
def add(request):
    form = forms.calendars.Event(request.POST)

    if len(request.POST) == 0 or not form.validate():
        if len(request.POST) == 0:
            form.tags.data = ['Event']
        tags = models.Topic.objects().distinct('tags')
        return dict(form=form, tags=json.dumps(tags))
    
    topic = models.Topic(**form.data)
    event = models.Event(**form.data)
    event.topic = topic
    event.author = request.user
    event.ip_address = request.environ['REMOTE_ADDR']
    return HTTPFound(location=request.route_path('manager.events.index'))
