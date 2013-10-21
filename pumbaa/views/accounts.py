'''
Created on Oct 13, 2013

@author: boatkrap
'''

from pyramid.view import view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pyramid.security import remember, forget

from pumbaa import models, forms

import mongoengine as me

@view_config(route_name='register', renderer='/accounts/register.mako')
def register(request):
    form = forms.accounts.Register(request.POST)
    
    if len(request.POST) > 0 and form.validate():
        password = form.data.get('password')
    else:
        return dict(
                form=form
                )
        
    user = models.User(**form.data)
    user.set_password(password)
    role = models.Role.objects(name='anonymous').first()
    user.roles.append(role)
    user.ip_address = request.environ['REMOTE_ADDR']
    user.save()
    
    return HTTPFound(location=request.route_path('index'))

@view_config(route_name='login', renderer='/accounts/login.mako')
@forbidden_view_config(renderer='/accounts/login.mako')
def login(request):
    if request.user:
        return HTTPFound(location=request.route_path('home'))
    
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/'
        
    came_from = request.params.get('came_from', referrer)
    message = ''
    session = request.session
    session['came_from'] = came_from
    
    form = forms.accounts.Login(request.POST)

    if len(request.POST) > 0 and form.validate():
        username = form.data.get('username')
        password = form.data.get('password')
        came_from = form.data.get('came_from')

        hash_password = request.secret_manager.get_hash_password(password)
        user = models.User.objects((me.Q(username=username) | me.Q(email=username))\
                                    & me.Q(password=hash_password)\
                                    & me.Q(status__ne='delete')).first()

        if user:
            headers = remember(request, str(user.id))
            if came_from == '/':
                came_from = request.route_path('home')
            
            if 'came_from' in session:
                del session['came_from']
                
            return HTTPFound(location = came_from,
                             headers = headers)
        else:
            message = 'Username or password mismatch'

    form.came_from.data = came_from
    
    return dict(
                form=form,
                message=message
                )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('index'),
                     headers = headers)

@view_config(route_name='home', renderer='/accounts/home.mako', permission='login')
def home(request):
    return dict()

@view_config(
    context='velruse.AuthenticationComplete',
)
def online_login_complete(request):
    context = request.context

    domain = context.profile["accounts"][0]['domain']
    user_id  = context.profile["accounts"][0]['userid']

    print("profile_type:", domain, "userid:", user_id)
    
    user = None
    user = models.User.objects(online_profiles__domain='facebook.com',\
                                online_profiles__user_id=str(user_id)).first()
    
    new_user = False
    if not user:
        new_user = True
        user = models.User()
        profile = models.Profile()
        profile.user_id = user_id
        profile.domain = domain
        
        user.first_name = context.profile['name']['givenName']
        user.last_name = context.profile['name']['familyName']
        user.email = context.profile['verifiedEmail']
        user.online_profiles.append(profile)
        user.default_profile = domain
        user.roles.append(models.Role.objects(name="anonymous").first())
    
        check_display_name = models.User.objects(username = context.profile['displayName']).first()
        if not check_display_name:
            user.username = context.profile['displayName']
        else:
            user.username = context.profile['displayName']+"_"

    profile = user.get_profile(domain)
    profile.first_name   = context.profile['name']['givenName']
    profile.last_name    = context.profile['name']['familyName']
    profile.display_name = context.profile['displayName']
    profile.username     = context.profile['preferredUsername']
    profile.email        = context.profile['verifiedEmail']
    
    profile.profile_source = context.profile
    
    user.save()
    user.reload()
    headers = remember(request, str(user.id))

    if user.status == 'wait for approval':
        new_user = True
        
    if new_user:
        return HTTPFound(location = request.route_path('home'),
                     headers = headers)
    
    
    session = request.session
    location = request.route_path('home')
    
    if "came_from" in session:
        if request.route_path('login') not in session['came_from']:
            location = session['came_from']
        del session['came_from']

    return HTTPFound(location = location,
                     headers = headers)
    
@view_config(
    context='velruse.AuthenticationDenied',
    renderer='/account/result.mako',
)

def login_denied_view(request):
    return Response({
        'result': 'denied',
    })
