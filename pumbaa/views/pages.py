'''
Created on Oct 20, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pumbaa import models

@view_config(route_name='pages.index', 
             renderer='/pages/index.mako')
def index(request):
    topics = models.Topic.objects(status__ne='delete', page=True).all()
    return dict(
                topics=topics
                )
    
@view_config(route_name='pages.view', 
             renderer='/pages/view.mako')
def view(request):
    title = request.matchdict.get('title')
    try:
        topic = models.Topic.objects(title__iexact=title, page=True, status='publish').first()
        if topic is None:
            raise 'Not floud'
    except:
        return Response('Not Found, topic title:%s'%title, status='404 Not Found')
        
    return dict(
                topic=topic
                )