'''
Created on May 23, 2014

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

@view_config(route_name='calendars.calendars.index', renderer='/calendars/calendars/index.mako')
def index(request):
    request.response.headerlist.extend(
            (
                ('Access-Control-Allow-Origin', '*')
            )
    )
    return dict()