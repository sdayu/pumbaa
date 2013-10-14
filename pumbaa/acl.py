'''
Created on Oct 13, 2013

@author: boatkrap
'''
from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid.security import Authenticated
from pyramid.security import ALL_PERMISSIONS

class RootFactory(object):

    @property
    def __acl__(self):
        
        acls = [(Allow, Authenticated, 'login'),
               (Allow, 'r:admin', ALL_PERMISSIONS) ]

        return acls

    def __init__(self, request):
        pass
