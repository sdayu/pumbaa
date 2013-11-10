'''
Created on Oct 19, 2013

@author: boatkrap
'''
from wtforms import Form
from wtforms import fields
from wtforms import validators

class Forum(Form):
    name = fields.TextField('Name', validators=[validators.InputRequired()])
    description = fields.TextAreaField('Description', validators=[validators.InputRequired()])
    tags = fields.HiddenField('Process tags', validators=[validators.InputRequired()])
    
    def get_topics(self, limit=0):
        from .topics import Topic
        topics = opic.objects(tags__in=self.tags, status='publish').order_by('-published_date')
        if limit != 0:
            topics.limit(limit)
            
        return topics