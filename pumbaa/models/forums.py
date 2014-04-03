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
    
    def get_topic(self):
        topic = Topic.objects(comments__id = self.id).first()
        if topic is None:
            topic = Topic.objects(comments__replies__id = self.id).first()
        if topic is None:
            topic = Topic.objects(comments__replies__replies__id = self.id).first()
        return topic
        
    
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
    
    def get_comment(self, comment_id):
        
        def find_comment(comment_id, comments): 
            # print("comments", len(comments))
            # print("comment id:", comment_id) 
            for comment in comments:
                print("check id:", comment.id) 
                if str(comment.id) == comment_id:
                    print("found")
                    return comment
                else:
                    if len(comment.replies) > 0:
                        # print("==>", len(comment.replies))
                        comment = find_comment(comment_id, comment.replies)
                        if comment:
                            return comment
                    # print("check again")
                    
             
        return find_comment(comment_id, self.comments)
            
    
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
    
    def get_topics(self, limit=None, skip=None):
        topics = Topic.objects(tags__in=self.tags, status='publish').order_by('-published_date')
        if limit:
            topics = topics.limit(limit)
        if skip:
            topics = topics.skip(skip)
        
        return topics