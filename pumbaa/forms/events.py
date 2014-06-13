from wtforms import Form
from wtforms import fields
from wtforms import validators

from pumbaa import models

from pyramid.threadlocal import get_current_request
from pyramid.security import has_permission

from . import topics

class RepeatableEvent(Form):
    repeats = fields.StringField('Repeats')
    ## every = fields.IntegerField('Repeat Every', default=1, validators=[validators.InputRequired()])
    on = fields.StringField('Repeat On')
    end = fields.StringField('End')
    
    

class Event(topics.Topic):
    started_date = fields.DateTimeField('Start Date', format='%d/%m/%Y %H:%M', validators=[validators.InputRequired()])
    ended_date = fields.DateTimeField('End Date', format='%d/%m/%Y %H:%M', validators=[validators.InputRequired()])
    
    venue = fields.StringField('Where')

    all_day = fields.BooleanField()
    repeat = fields.BooleanField()
    repeat = fields.FormField(RepeatableEvent)
    
    event_type = fields.SelectField('Event Type', validators=[validators.InputRequired()], 
                                    choices=[(t, t.title()) for t in models.events.EVENT_TYPES])


