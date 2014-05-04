from wtforms import Form
from wtforms import fields
from wtforms import validators

from pumbaa import models

from pyramid.threadlocal import get_current_request
from pyramid.security import has_permission

class Event(Form):
    title = fields.TextField('Title', validators=[validators.InputRequired()])
    description = fields.TextAreaField('Description', validators=[validators.InputRequired()])
    # tags = fields.TextField('Tags', validators=[validators.InputRequired()])
    tags = fields.HiddenField('Tags', validators=[validators.InputRequired()])
    started_date = fields.DateTimeField('Start Date', validators=[validators.InputRequired()])
    ended_date = fields.DateTimeField('End Date', validators=[validators.InputRequired()])

    all_day = fields.BooleanField()
    repeat = fields.BooleanField()


