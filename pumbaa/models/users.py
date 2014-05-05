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
    
    registration_date = me.DateTimeField(required=True, default=datetime.datetime.now)

class Approver(me.EmbeddedDocument):
    user = me.ReferenceField("User", dbref=True, required=True)
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
    display_name = me.StringField(max_length=250, required=True)
    
    default_profile = me.StringField(default='pumbaa.coe.psu.ac.th')
    online_profiles = me.ListField(me.EmbeddedDocumentField(Profile))
    
    status = me.StringField(max_length=100, required=True, default='wait for approval')
    
    registration_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    approvers = me.ListField(me.EmbeddedDocumentField(Approver))
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    roles = me.ListField(me.ReferenceField('Role', dbref=True))
    
    def get_display_name(self):
        if self.display_name is not None:
            return self.display_name
        else:
            return self.username

    def get_tim_display_name(self):
        tname = self.get_display_name().split(" ")
        if len(tname) > 1:
            return "%s. %s" % (tname[0][0],tname[1])
        else:
            return "%s" % (tname[0])
        
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
            
    def get_profile_picture_url(self, width=50):
        if self.default_profile == 'pumbaa.coe.psu.ac.th':
            return "#"

        return "#"

    def get_profile_picture(self, width=50):
        if self.default_profile == 'pumbaa.coe.psu.ac.th':
            return None
        profile = self.get_profile(self.default_profile)
        if profile.domain == 'facebook.com':
            if '=' in profile.username:
                username = profile.username.split('=')[-1]
            else:
                username = profile.username
            return '<img src="https://graph.facebook.com/%s/picture" width="%d"/>'%(username, width)
        if profile.domain == 'twitter.com':
            return '<img src="%s" width="%d"/>'%(profile.profile_source['photos'][0]['value'], width)
        if profile.domain == 'accounts.google.com':
            return '<img src="%s" width="%d"/>'%(profile.profile_source['photos'][0]['value'], width)
        return None
    
    def get_profile_url(self):
        if self.default_profile == 'pumbaa.coe.psu.ac.th':
            return '#'
        profile = self.get_profile(self.default_profile)
        if profile.domain == 'facebook.com':
            return 'https://www.facebook.com/%s'%profile.username
        if profile.domain == 'twitter.com':
            return 'https://twitter.com/%s'%profile.username
        if profile.domain == 'accounts.google.com':
            return 'https://plus.google.com/%s'%profile.user_id
        return '#'
        
class Role(me.Document):
    meta = {'collection' : 'roles'}
    
    name = me.StringField(max_length=100, required=True)
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
