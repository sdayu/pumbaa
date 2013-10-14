'''
Created on Oct 13, 2013

@author: boatkrap
'''
'''
Created on Jan 28, 2013

@author: boatkrap
'''
from wtforms import fields
from wtforms import validators
from wtforms.fields import html5

from pumbaa import models

from wtforms.form import Form

def validate_email(form, field):
    user = models.User.objects(email=field.data).first()

    if user is not None:
        raise validators.ValidationError(
            'This email: %s is available on system'% field.data)

def validate_username(form, field):
    user = models.User.objects(username=field.data).first()

    if user is not None:
        raise validators.ValidationError(
            'This user: %s is available on system'% field.data)
     
class Register(Form):
    username = fields.TextField('Username', validators=[validators.InputRequired(), validate_username])
    email = html5.EmailField('Email', validators=[validators.InputRequired(), validators.Email(), validate_email])
    password = fields.PasswordField('Password', validators=[validators.InputRequired(), validators.EqualTo('password_conf', message="password mismatch")])
    password_conf = fields.PasswordField('Password Confirm', validators=[validators.InputRequired()])
    first_name = fields.TextField('First name', validators=[validators.InputRequired()])
    last_name = fields.TextField('Last name', validators=[validators.InputRequired()])
    