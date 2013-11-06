'''
Created on Oct 19, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models

@view_config(route_name='forums.tags.index', renderer="/forums/tags/index.mako")
def index(request):
    tags = models.Topic.objects.distinct('tags')
    return dict(
                tags=tags
            )
    
@view_config(route_name='forums.tags.list_contents', renderer="/forums/tags/list_contents.mako")
def list_contents(request):
    name = request.matchdict.get('name')
    topics = models.Topic.objects(tags=name, status='publish').all()
    return dict(
                tag=name,
                topics=topics
            )