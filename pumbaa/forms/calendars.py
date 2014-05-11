from wtforms import Form
from wtforms import fields
from wtforms import validators

from pumbaa import models

from pyramid.threadlocal import get_current_request
from pyramid.security import has_permission

from . import topics

class Event(topics.Topic):
    started_date = fields.DateTimeField('Start Date', validators=[validators.InputRequired()])
    ended_date = fields.DateTimeField('End Date', validators=[validators.InputRequired()])
    
    place = fields.StringField('Where')

    all_day = fields.BooleanField()
    repeat = fields.BooleanField()
    
    event_type = fields.SelectField('Event Type', validators=[validators.InputRequired()], 
                                    choices=[(t, t.title()) for t in models.calendars.EVENT_TYPES])


