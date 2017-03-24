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

# @view_config(route_name='forums.tags.index', renderer="/forums/tags/index.mako")
def index(request):
    tags = models.Topic.objects.distinct('tags')
    return dict(
                tags=tags
            )
    
# @view_config(route_name='forums.tags.list_contents', renderer="/forums/tags/list_contents.mako")
def list_contents(request):
    name = request.matchdict.get('name')
    topics = models.Topic.objects(tags=name, status='publish').all()
    return dict(
                tag=name,
                topics=topics
            )
