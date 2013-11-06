'''
Created on Oct 13, 2013

@author: boatkrap
'''
from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid.security import Authenticated
from pyramid.security import ALL_PERMISSIONS

from pumbaa import models

def group_finder(userid, request):

    user = models.User.objects(id=userid).first()
    
    if user:
        return ["role:%s"%role.name for role in user.roles]
    
class RootFactory(object):

    @property
    def __acl__(self):
        
        acls = [(Allow, Authenticated, 'login'),
               (Allow, 'role:admin', ALL_PERMISSIONS)]
        
        roles = models.Role.objects.all()
        for role in roles:
            acls.append((Allow, 'role:'+role.name, role.name))
            
            if role.name in ['admin', 'lecturer', 'staff', 'moderator']:
                acls.append((Allow, 'role:'+role.name, 'page'))
                acls.append((Allow, 'role:'+role.name, 'topic'))
                acls.append((Allow, 'role:'+role.name, 'announce-tag'))
        

        return acls

    def __init__(self, request):
        pass
