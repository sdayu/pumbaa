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
    tags = fields.TextField('Process tags', validators=[validators.InputRequired()])