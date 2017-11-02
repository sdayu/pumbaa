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

from . import tags
from . import topics
from . import feeds

url_prefix = '/forums'
module = Blueprint('forums', __name__, url_prefix=url_prefix)

def register_blueprint(app):
    app.register_blueprint(module)

    for view in [tags,
                 topics,
                 feeds]:

        if 'register_blueprint' in dir(view):
            view.register_blueprint(app, url_prefix)
        else:
            app.register_blueprint(
                view.module,
                url_prefix=url_prefix + view.module.url_prefix)



from .. import topicutils
@module.route('/')
def index():
    forums = models.Forum.objects(status='publish').all()
    return render_template('/forums/forums/index.jinja2',
                forums=forums,
                topicutils=topicutils
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
                topicutils=topicutils,
                page=page,
                pages=pages
                )
