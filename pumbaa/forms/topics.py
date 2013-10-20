'''
Created on Oct 18, 2013

@author: boatkrap
'''
from wtforms import Form
from wtforms import fields
from wtforms import validators

from pumbaa import models

from pyramid.threadlocal import get_current_request

def available_page_title(form, field):
    topic = models.Topic.objects(title=field.data, page=True).first()
    
    request = get_current_request()
    topic_id = request.matchdict.get('topic_id', None)
    if topic_id is not None:
        if str(topic.id) == topic_id:
            # edit case
            return
    
    if topic is not None:
        raise validators.ValidationError(
            'This page title: %s is available on system'% field.data)

class Topic(Form):
    title = fields.TextField('Title', validators=[validators.InputRequired()])
    description = fields.TextAreaField('Description', validators=[validators.InputRequired()])
    tags = fields.TextField('Tags', validators=[validators.InputRequired()])

class Page(Topic):
    title = fields.TextField('Title', validators=[validators.InputRequired(), available_page_title])
    comments_disable = fields.RadioField('Is disable comments', 
                                         choices=[('enable', 'enable'), ('disable', 'disable')],
                                         validators=[validators.InputRequired()])

class Comment(Form):
    message = fields.TextAreaField('Message', validators=[validators.InputRequired()])