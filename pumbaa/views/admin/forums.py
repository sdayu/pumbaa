'''
Created on Oct 19, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models, forms

import json
import datetime

@view_config(route_name='admin.forums.index', 
             permission='admin', 
             renderer='/admin/forums/index.mako')
def index(request):
    forums = models.Forum.objects(status__ne='delete').all()
    return dict(
                forums=forums
                )
    
@view_config(route_name='admin.forums.create', 
             permission='admin', 
             renderer='/admin/forums/create.mako')
@view_config(route_name='admin.forums.edit', 
             permission='admin', 
             renderer='/admin/forums/create.mako')
def create(request):
    forum_id = request.matchdict.get('forum_id', None)
    
    form = forms.forums.Forum(request.POST)
    
    if len(request.POST) == 0 or not form.validate():
        tags = models.Topic.objects().distinct('tags')
        tags.extend(models.Forum.objects().distinct('tags'))
        
        if forum_id is not None:
            forum = models.Forum.objects.with_id(forum_id)
            form.name.data = forum.name
            form.description.data = forum.description
            form.tags.data = " ,".join(forum.tags)
        
        return dict(
                tags = json.dumps(tags),
                form=form
                )
    else:
        name = form.data.get('name')
        description = form.data.get('description')
        tags = [tag.strip() for tag in form.data.get('tags').split(',')]
        
    if forum_id:
        forum = models.Forum.objects.with_id(forum_id)
        forum.name = name
        forum.description = description
        forum.tags = tags
        forum.updated_date = datetime.datetime.now()
    else:
        forum = models.Forum(name=name, 
                         description=description, 
                         tags=tags, 
                         author=request.user)
    forum.save()
    
    return HTTPFound(location=request.route_path('forums.view', name=forum.name))

@view_config(route_name='admin.forums.delete', 
             permission='admin')
def delete(request):
    forum_id = request.matchdict.get('forum_id')
    forum = models.Forum.objects().with_id(forum_id)
    forum.status = 'delete'
    forum.updated_date = datetime.datetime.now()
    forum.save()
    
    return HTTPFound(location=request.route_path('admin.forums.index'))
    