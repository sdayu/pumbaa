'''
Created on Oct 20, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models, forms

@view_config(route_name='admin.users.index', 
             permission='admin', 
             renderer='/admin/users/index.mako')
def index(request):
    users = models.User.objects(status__ne='delete').order_by('-username').all()
    return dict(
                users=users
                )
    
@view_config(route_name='admin.users.add_role', 
             permission='admin', 
             renderer='/admin/users/add_role.mako')
def add_role(request):
    user_id = request.matchdict.get('user_id')
    role_id = request.matchdict.get('role_id')
    
    user = models.User.objects.with_id(user_id)
    role = models.Role.objects.with_id(role_id)
    
    if role.name != 'anonymous':
        if role not in user.roles:
            user.roles.append(role)
            user.save()
    
    return HTTPFound(location=request.route_path('admin.users.index'))