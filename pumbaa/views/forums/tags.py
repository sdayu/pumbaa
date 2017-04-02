'''
Created on Oct 19, 2013

@author: boatkrap
'''

from flask import Blueprint, render_template, request, redirect, make_response, current_app, url_for
from authomatic.adapters import WerkzeugAdapter

from flask_login import login_required, current_user, login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity


from pumbaa import models

module = Blueprint('forums.tags', __name__, url_prefix='/tags')

@module.route('/')
def index():
    tags = models.Topic.objects.distinct('tags')
    return render_template('/forums/tags/index.jinja2',
                tags=tags
            )
    
@module.route('/<name>')
def list_contents(name):
    topics = models.Topic.objects(tags=name, status='publish').all()
    return render_template('/forums/tags/list-contents.jinja2',
                tag=name,
                topics=topics
            )
