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

class User(me.Document):
    meta = {'collection' : 'users'}
    
    username = me.StringField(required=True, unique=True)
    password = me.StringField()
    email = me.EmailField(required=True, unique=True)
    first_name = me.StringField(max_length=100, required=True)
    last_name = me.StringField(max_length=100)
    
    online_profiles = me.MapField(field=me.EmbeddedDocumentField(Profile))
    
    status = me.StringField(max_length=100, required=True, default="wait for approval")
    
    registration_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    roles = me.ListField(me.ReferenceField('Role', dbref=True))
    
    def set_password(self, password):
        from pyramid.threadlocal import get_current_request
        request = get_current_request()
        self.password = request.secret_manager.get_hash_password(password)
        
        
class Role(me.Document):
    meta = {'collection' : 'roles'}
    
    name = me.StringField(max_length=100, required=True)
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    