'''
Created on Oct 18, 2013

@author: boatkrap
'''
from flask import Blueprint, render_template, request, redirect, make_response, current_app, url_for
from authomatic.adapters import WerkzeugAdapter

from flask_login import login_required, current_user, login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity

from pumbaa import models, forms
import json
import math

module = Blueprint('forums.topics', __name__)

# @view_config(route_name='forums.topics.index', 
#              renderer='/forums/topics/index.mako')
@module.route('/')
def index():
    page = int(request.args.get('page', 1))
    topics_per_page = 15
    
    topic_count = models.Topic.objects(status='publish').count()
    pages = math.ceil(topic_count/topics_per_page)
    
    page = page if page > 0 else 1
    page = page if page <= pages else pages
    
    topics = models.Topic.objects(status='publish').order_by('-published_date').skip((page-1)*topics_per_page).limit(topics_per_page).all()
    return render_template('/forums/topics/index.jinja2',
                topics=topics,
                pages=pages,
                page=page
                )

# @view_config(route_name='forums.topics.view', 
#              renderer='/forums/topics/view.mako')
@module.route('/<topic_id>/<title>')
def view(topic_id, title):
    
    topic = models.Topic.objects(id=topic_id, status='publish').first()
    
    if topic is None:
        return Response('Not Found, topic title:%s'%title, status='404 Not Found')
        
    return render_template('/forums/topics/view.jinja2',
            topic=topic
            )
