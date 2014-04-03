'''
Created on Nov 10, 2013

@author: boatkrap
'''
from wtforms import Form
from wtforms import fields
from wtforms.fields import html5
from wtforms import validators
import re
import datetime

class PhotoAlbum(Form):
    name = fields.TextField('Name', validators=[validators.InputRequired()])
    description = fields.TextAreaField('Description')
    shared = fields.BooleanField()
    event_date = html5.DateField(default=datetime.datetime.now())
    
    
class Photo(Form):
    image = fields.FileField('Image')
    license = fields.SelectField('License', validators=[validators.InputRequired()])
    