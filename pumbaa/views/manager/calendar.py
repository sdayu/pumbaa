from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pumbaa import models
from pumbaa import forms
@view_config(route_name='manager.calendars.index', 
             permission='member',
             renderer='/manager/calendars/index.mako')
def index(request):
    topics = models.Topic.objects(status__ne='delete', author=request.user).all()
    return dict(
                topics=topics
                )

@view_config(route_name='manager.calendars.add', 
             permission='member',
             renderer='/manager/calendars/event.mako')
def add(request):
	form = forms.calendars.Event(request.POST)
	if len(request.POST) == 0 and not form.validate():
		return dict(form=form)
    return dict(
                topics=topics
                )
