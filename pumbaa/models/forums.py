import mongoengine as me

import datetime
import bson

# class Tag(me.Document):
#     meta = {'collection' : 'tags'}
#     
#     name = me.StringField(required=True)
#     created_date = me.DateTimeField(required=True, default=datetime.datetime.now)

class Comment(me.EmbeddedDocument):
    id = me.ObjectIdField(required=True, default=bson.ObjectId)
    message = me.StringField(required=True)
    replies = me.ListField(me.EmbeddedDocumentField("Comment"))
    
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    status = me.StringField(required=True, default='draft')
    """ status: draft, publish, delete """
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    author = me.ReferenceField("User", dbref=True)
    
class TopicHistory(me.EmbeddedDocument):
    author = me.ReferenceField("User", dbref=True, required=True)
    changed_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    title = me.StringField(required=True)
    description = me.StringField(required=True)
    tags = me.ListField(me.StringField(required=True), required=True)

class Topic(me.Document):
    meta = {'collection' : 'topics'}
    
    title = me.StringField(required=True)
    description = me.StringField(required=True)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField()
    
    status = me.StringField(required=True, default='draft')
    """ status: draft, publish, delete """
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')

    author = me.ReferenceField("User", dbref=True, required=True)

    comments = me.ListField(me.EmbeddedDocumentField(Comment))
    tags = me.ListField(me.StringField(required=True), required=True)
    
    page = me.BooleanField(default=False, required=True)
    comments_disabled = me.BooleanField(default=False, required=True)
    
    histories = me.ListField(me.EmbeddedDocumentField(TopicHistory))
    
class Forum(me.Document):
    meta = {'collection' : 'forums'}
    
    name = me.StringField(required=True, unique=True)
    description = me.StringField()
    tags = me.ListField(me.StringField(required=True), required=True)
    status = me.StringField(required=True, default="publish")
    """ status: publish, delete """
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    author = me.ReferenceField("User", dbref=True, required=True)
    
    def get_topics(self, limit=None):
        topics = Topic.objects(tags__in=self.tags, status='publish').order_by('-published_date')
        if limit:
            topics = topics.limit(limit)
        
        return topics