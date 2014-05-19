import json

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pumbaa import models
from pumbaa import forms

@view_config(route_name='manager.calendars.index', 
             permission='member',
             renderer='/manager/calendars/index.mako')
def index(request):
    topics = []
    return dict(
                topics=topics
                )

@view_config(route_name='manager.calendars.add', 
             permission='member',
             renderer='/manager/calendars/event.mako')
def add(request):
    form = forms.calendars.Event(request.POST)
    print(len(request.POST))
    if len(request.POST) == 0 or not form.validate():
        if len(request.POST) == 0:
            form.tags.data = ['Event']
        tags = models.Topic.objects().distinct('tags')
        return dict(form=form, tags=json.dumps(tags))
    
    return HTTPFound(location=request.route_path('manager.calendars.index'))
