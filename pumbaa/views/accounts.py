'''
Created on Oct 13, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pumbaa import models, forms

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
def login(request):
    return dict()

@view_config(route_name='home', renderer='/accounts/home.mako', permission='login')
def home(request):
    return dict()