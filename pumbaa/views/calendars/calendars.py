'''
Created on May 23, 2014

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
import mongoengine as me

import datetime

from pumbaa import models


@view_config(route_name='calendars.calendars.index', renderer='/calendars/calendars/index.mako')
def index(request):
    request.response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
#         'Access-Control-Max-Age': '1728000',
        })

    return dict()

@view_config(route_name='calendars.calendars.agenda', renderer='/calendars/calendars/agenda.mako')
def agenda(request):
    events =     events = models.Event.objects((me.Q(status='publish') &
                                  (me.Q(started_date__gt=datetime.datetime.now().date()) | 
                                  me.Q(ended_date__gt=datetime.datetime.now())) &
                                  me.Q(event_type__ne='conference')))\
                        .order_by('+started_date')\
                        .all()
    return dict(events=events)