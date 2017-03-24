'''
Created on Oct 18, 2013

@author: boatkrap
'''
from flask import Blueprint, render_template, request, redirect, make_response, current_app, url_for
from authomatic.adapters import WerkzeugAdapter

from flask_login import login_required, current_user, login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity


from pumbaa import models
import math


from .. import app
from . import tags
from . import topics
from . import feeds

default_prefix = '/forums'
module = Blueprint('forums', __name__, url_prefix=default_prefix)
app.register_blueprint(tags.module, url_prefix=default_prefix+'/tags')
app.register_blueprint(topics.module, url_prefix=default_prefix+'/topics')
app.register_blueprint(feeds.module, url_prefix=default_prefix+'/feeds')

# @view_config(route_name='forums.index', 
#              renderer='/forums/forums/index.mako')
@module.route('/')
def index():
    forums = models.Forum.objects(status='publish').all()
    return dict('/forums/forums/index.jinja2',
                forums=forums
                )
    
# @view_config(route_name='forums.view', 
#              renderer='/forums/forums/view.mako')
@module.route('/view/<name>')
def view(name):
    forum = models.Forum.objects(name=name, status='publish').first()
    if forum is None:
        return Response('Forum name: %s not found!'%name, status='404 Not Found')
    
    
    page = int(request.args.get('page', 1))
    topics_per_page = 15
    
    topic_count = models.Topic.objects(tags__in=forum.tags, status='publish').count()
    pages = math.ceil(topic_count/topics_per_page)
    
    page = page if page > 0 else 1
    page = page if page <= pages else pages
    
    topics = models.Topic.objects(tags__in=forum.tags, status='publish').order_by('-published_date').skip((page-1)*topics_per_page).limit(topics_per_page).all()
    
    
    return render_template('/forums/forums/view.jinja2',
                forum=forum,
                topics=topics,
                page=page,
                pages=pages
                )
