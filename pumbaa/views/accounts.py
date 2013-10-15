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
    print('test')
    form = forms.accounts.Register(request.POST)
    
    if len(request.POST) > 0 and form.validate():
        password = form.data.get('password')
    else:
        return dict(
                form=form
                )
        
    user = models.User(**form.data)
    user.password = request.secret_manager.get_hash_password(password)
    role = models.Role.objects(name='member').first()
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
    
    form = forms.accounts.Login(request.POST)

    if len(request.POST) > 0 and form.validate():
        username = form.data.get('username')
        password = form.data.get('password')
        came_from = form.data.get('came_from')

        hash_password = request.secret_manager.get_hash_password(password)
        user = models.User.objects((me.Q(username=username) | me.Q(email=username))\
                                    & me.Q(password=hash_password)).first()

        if user:
            headers = remember(request, str(user.id))
            if came_from == '/':
                came_from = request.route_path('home')
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
    print("This is home")
    return dict()