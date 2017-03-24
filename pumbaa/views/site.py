from flask import Blueprint, render_template, request, redirect, make_response, current_app, url_for
from authomatic.adapters import WerkzeugAdapter

from flask_login import login_required, current_user, login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity

import math
import datetime

from .. import authomatic
from pumbaa import models
from pumbaa import forms

import mongoengine as me

module = Blueprint('site', __name__)

from . import topicutils

@module.route('/')
def index():
    recent_topics = models.Topic.objects(status='publish', type='topic').order_by('-published_date').limit(10).all()
    last_comments_topics_ = models.Topic.objects(status='publish', type='topic').order_by('-comments__published_date').limit(10).all()
    last_comments_topics = []
    for topic in last_comments_topics_:
        try:
            if len(topic.comments) > 0:
                last_comments_topics.append(topic)
        except Exception as e:
            print(e)
    
    photo_albums_ = models.PhotoAlbum.objects(status='publish').order_by('-published_date').limit(10).all()
    photo_albums = []
    for photo_album in photo_albums_:
        if len(photo_album.photos)> 0:
            photo_albums.append(photo_album)
            
    events = models.Event.objects((me.Q(status='publish') &
                                  (me.Q(started_date__gt=datetime.datetime.now().date()) | 
                                  me.Q(ended_date__gt=datetime.datetime.now())) &
                                  me.Q(event_type__in=['undergraduate', 'graduate', 'department'])))\
                        .order_by('+started_date')\
                        .limit(5).all()
    
    dep_announcement = models.Forum.get_forum('ประกาศจากภาควิชา')

    return render_template('/site/index.jinja2',
            dep_announcement=dep_announcement,
		   	recent_topics=recent_topics,
            last_comments_topics=last_comments_topics,
            photo_albums=photo_albums,
            events=events,
            topicutils=topicutils
            )
#            literatures=literatures,
#            num_rows=num_rows)

# @module.route('/login')
# def login():

#     form = forms.accounts.Login(request.form)    
    
#     return render_template('/site/login.jinja2', form=form)




# @module.route('/login/<provider_name>/', methods=['GET', 'POST'])
# def do_login(provider_name):
#     """
#     Login handler, must accept both GET and POST to be able to use OpenID.
#     """
#     if provider_name == 'pumbaa':
#         return

#     # We need response object for the WerkzeugAdapter.
#     response = make_response()

#     # Log the user in, pass it the adapter and the provider name.
#     result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

#     # If there is no LoginResult object, the login procedure is still pending.
#     if result:
#         if result.user:
#             # We need to update the user to get more info.
#             result.user.update()

#             print('result =>', result.user.provider.name)
#             print('data   =>', result.user.data)
#             # flask login
#             # login_user(user)
#             user = models.User.objects(email=result.user.email).first()


#             if not user:
#                 parameters = {
#                         'providers__%s__id'%result.user.provider.name: result.user.data['id']
#                         }

#             if not user:
#                 user = models.User(
#                         email=result.user.email,
#                         username=result.user.name,
#                         birth_date=result.user.birth_date,
#                         name=result.user.name,
#                         first_name=result.user.first_name,
#                         last_name=result.user.last_name,
#                         gender=result.user.gender
#                         )

#             if not user.email:
#                 email=result.user.email
#                 username=result.user.name
#                 birth_date=result.user.birth_date
#                 name=result.user.name
#                 first_name=result.user.first_name
#                 last_name=result.user.last_name
#                 gender=result.user.gender


#             user.providers[result.user.provider.name] = result.user.data
#             user.save()

#             login_user(user)
#             identity_changed.send(current_app._get_current_object(),
#                     identity=Identity(str(user.id)))

#         nextx = request.args.get('next')
#         return redirect(nextx or url_for('dashboard.index'))
#         # The rest happens inside the template.
#         # return render_template('/site/login-success.jinja2', result=result)

#     # Don't forget to return the response.
#     return response

# @module.route('/logout')
# @login_required
# def logout():
#     # Remove the user information from the session
#     logout_user()

#     # Remove session keys set by Flask-Principal
#     for key in ('identity.name', 'identity.auth_type'):
#         session.pop(key, None)

#     # Tell Flask-Principal the user is anonymous
#     identity_changed.send(current_app._get_current_object(),
#                           identity=AnonymousIdentity())

#     return redirect(request.args.get('next') or '/')
