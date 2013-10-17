'''
Created on Oct 17, 2013

@author: boatkrap
'''
from pumbaa import models

from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid, authenticated_userid

from . import cryto

class RequestWithUserAttribute(Request):
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid is not None:
            user = models.User.objects(id=userid).first()
            return user
        
    @reify
    def userid(self):
        return authenticated_userid(self)
    
    @reify
    def secret_manager(self):
        from pyramid.threadlocal import get_current_registry
        settings = get_current_registry().settings
        
        return cryto.SecretManager(settings.get('pumbaa.secret', None))