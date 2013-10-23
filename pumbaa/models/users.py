'''
Created on Oct 11, 2013

@author: boatkrap
'''

import mongoengine as me

import datetime

class Profile(me.EmbeddedDocument):
    domain = me.StringField(required=True, unique=True)
    user_id = me.StringField(required=True)
    email = me.EmailField(required=True)
    first_name = me.StringField()
    last_name = me.StringField()
    username = me.StringField()
    display_name = me.StringField()
    
    profile_source = me.DictField()

class Approver(me.EmbeddedDocument):
    user = me.ReferenceField("User", required=True)
    approved_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    ip_address = me.StringField(max_length=100, required=True, default='0.0.0.0')

class User(me.Document):
    """
    status  : 'wait for approval' -> wait member approve this profile
            : 'activate' -> this profile are approve
    """
    
    meta = {'collection' : 'users'}
    
    username = me.StringField(required=True, unique=True)
    password = me.StringField()
    email = me.EmailField(required=True, unique=True)
    first_name = me.StringField(max_length=100, required=True)
    last_name = me.StringField(max_length=100, required=True)
    
    default_profile = me.StringField(default='pumbaa.coe.psu.ac.th')
    online_profiles = me.ListField(me.EmbeddedDocumentField(Profile))
    
    status = me.StringField(max_length=100, required=True, default='wait for approval')
    
    registration_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    approvers = me.ListField(me.EmbeddedDocumentField(Approver))
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    roles = me.ListField(me.ReferenceField('Role', dbref=True))
    
    def set_password(self, password):
        from pyramid.threadlocal import get_current_request
        request = get_current_request()
        self.password = request.secret_manager.get_hash_password(password)
    
    def get_profile(self, domain):
        for profile in self.online_profiles:
            if profile.domain == domain:
                return profile
    
    def get_role(self, name):
        for role in self.roles:
            if role.name == name:
                return role
            
    def get_profile_picture(self, width=50):
        if self.default_profile == 'pumbaa.coe.psu.ac.th':
            return None
        profile = self.get_profile(self.default_profile)
        if profile.domain == 'facebook.com':
            return '<img src="https://graph.facebook.com/%s/picture" width="%d"/>'%(profile.username, width)
        if profile.domain == 'twitter.com':
            return '<img src="%s" width="%d"/>'%(profile.profile_source['photos'][0]['value'], width)
        if profile.domain == 'accounts.google.com':
            return '<img src="%s" width="%d"/>'%(profile.profile_source['photos'][0]['value'], width)
        return None
        
class Role(me.Document):
    meta = {'collection' : 'roles'}
    
    name = me.StringField(max_length=100, required=True)
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    