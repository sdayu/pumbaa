import mongoengine as me

import datetime
import bson

class Tag(me.Document):
    meta = {'collection' : 'tags'}
    
    name = me.StringField(required=True)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)

class Comment(me.EmbeddedDocument):
    id = me.ObjectIdField(required=True, default=bson.ObjectId)
    message = me.StringField(required=True)
    reply = me.ListField(me.EmbeddedDocumentField("Comment"))
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    author = me.ReferenceField("User", dbref=True)
    
    
class Topic(me.Document):
    meta = {'collection' : 'topic'}
    
    title = me.StringField(required=True)
    description = me.StringField(required=True)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')

    author = me.ReferenceField("User", required=True)
    comments = me.ListField(me.EmbeddedDocumentField(Comment))
    tags = me.ListField(me.ReferenceField(Tag, dbref=True))
            