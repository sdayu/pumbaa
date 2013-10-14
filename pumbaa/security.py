'''
Created on Oct 13, 2013

@author: boatkrap
'''
from pumbaa import models

def group_finder(userid, request):

    user = models.User.objects(id = userid).first()
    
    if user:
        return ["r:%s"%role.name for role in user.roles]

from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid, authenticated_userid

class RequestWithUserAttribute(Request):
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid is not None:
            user = models.User.objects(id = userid).first()
            return user
        
    @reify
    def userid(self):
        return authenticated_userid(self)
    
    @reify
    def secret_manager(self):
        from pyramid.threadlocal import get_current_registry
        settings = get_current_registry().settings
        
        return SecretManager(settings.get('pumbaa.secret', None))

import hashlib

class SecretManager:
    def __init__(self, secret):
        self.password_secret = secret

    def get_password_secret(self):
        return self.password_secret

        
    def get_hash_password(self, password):
        salt = hashlib.sha512(self.password_secret.encode('utf-8'))
        hash_pass = hashlib.sha512(password.encode('utf-8'))
        
        hash_pass.update((self.password_secret + salt.hexdigest()).encode('utf-8'))
        return hash_pass.hexdigest()
    