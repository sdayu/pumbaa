'''
Created on Oct 18, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models

@view_config(route_name='forums.index', 
             permission='member',
             renderer='/forums/forums/index.mako')
def index(request):
    return dict()