'''
Created on Oct 18, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models

@view_config(route_name='forums.index', 
             renderer='/forums/forums/index.mako')
def index(request):
    forums = models.Forum.objects(status='publish').all()
    return dict(
                forums=forums
                )
    
@view_config(route_name='forums.view', 
             renderer='/forums/forums/view.mako')
def view(request):
    name = request.matchdict.get('name')
    forum = models.Forum.objects(name=name, status='publish').first()
    topics = models.Topic.objects(tags__in=forum.tags).all()
    return dict(
                forum=forum,
                topics=topics
                )