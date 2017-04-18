'''
Created on Oct 18, 2013

@author: boatkrap
'''
# from wtforms import Form
from flask_wtf import Form
from wtforms import fields
from wtforms import validators

from pumbaa import models
from .fields import TagListField

#from pyramid.threadlocal import get_current_request
#from pyramid.security import has_permission

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

def announce_tag_allow(form, field):
    tags = field.data
    request = get_current_request()
    for tag in tags:
        if tag in ['ประกาศ', 'ประกาศจากภาควิชา', 'announce']:
            if not has_permission('announce-tag', request.context, request):
                raise validators.ValidationError(
                    'This tag name "%s" is not allowed'% tag)

class Topic(Form):
    title = fields.TextField('Title', validators=[validators.InputRequired()])
    description = fields.TextAreaField('Description', validators=[validators.InputRequired()])
    tags = TagListField('Tags', validators=[validators.InputRequired(), announce_tag_allow])

class Page(Topic):
    title = fields.TextField('Title', validators=[validators.InputRequired(), available_page_title])
    comments_disable = fields.RadioField('Is disable comments', 
                                         choices=[('enable', 'enable'), ('disable', 'disable')],
                                         validators=[validators.InputRequired()])

class Comment(Form):
    message = fields.TextAreaField('Message', validators=[validators.InputRequired()])
