'''
Created on Oct 17, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models

@view_config(route_name='manager.index', 
             permission='member', 
             renderer='/manager/index.mako')
def index(request):
    return dict()