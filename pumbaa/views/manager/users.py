'''
Created on Oct 17, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import has_permission
from pumbaa import models

@view_config(route_name='manager.users.approve', 
             permission='member', 
             renderer='/manager/users/approve.mako')
def approve(request):
    wait_for_approve = models.User.objects(status='wait for approval',
                                           approvers__user__ne=request.user).all()
    return dict(
                users=wait_for_approve
                )


@view_config(route_name='manager.users.do_approve', 
             permission='member')
def do_approve(request):
    APPROVE_THREDHOLD = 10
    
    user_id = request.matchdict['user_id']
    try:
        user = models.User.objects.with_id(user_id)
    except Exception as e:
        return HTTPFound(location=request.route_path('manager.users.approve'))
    
    
    approver = models.Approver(user=request.user,
                               ip_address=request.environ.get('REMOTE_ADDR'))
    user.approvers.append(approver)
    user.save()
    
    if len(user.approvers) >= APPROVE_THREDHOLD \
        or has_permission('admin', request.context, request)\
        or has_permission('moderator', request.context, request):
        
        user.status = 'activate'
        role = user.get_role('anonymous')
        user.roles.remove(role)
        role = models.Role.objects(name='member').first()
        user.roles.append(role)
        user.save()
    
    return HTTPFound(location=request.route_path('manager.users.approve'))