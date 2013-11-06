'''
Created on Oct 19, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models, forms

import json

@view_config(route_name='admin.forums.index', 
             permission='admin', 
             renderer='/admin/forums/index.mako')
def index(request):
    forums = models.Forum.objects().all()
    return dict(
                forums=forums
                )
    
@view_config(route_name='admin.forums.create', 
             permission='admin', 
             renderer='/admin/forums/create.mako')
def create(request):
    form = forms.forums.Forum(request.POST)
    
    if len(request.POST) == 0 or not form.validate():
        tags = models.Topic.objects().distinct('tags')
        tags.extend(models.Forum.objects().distinct('tags'))
        
        return dict(
                tags = json.dumps(tags),
                form=form
                )
    else:
        name = form.data.get('name')
        description = form.data.get('description')
        tags = [tag.strip() for tag in form.data.get('tags').split(',')]
    
    forum = models.Forum(name=name, 
                         description=description, 
                         tags=tags, 
                         author=request.user)
    forum.save()
    
    return HTTPFound(location=request.route_path('forums.view', name=forum.name))
    