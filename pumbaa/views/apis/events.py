'''
Created on Jun 24, 2014

@author: boatkrap
'''


from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

import datetime
from pumbaa import models

@view_defaults(route_name='apis.events', renderer='json')
class Events:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='apis.events.list', request_method='GET')
    def list_event(self):
        events = models.Event.objects(status='publish', 
                                  started_date__gt=datetime.datetime.now())\
                        .order_by('+started_date')\
                        .all()
        results = []
        for event in events:
            result = {'title': event.topic.title,
                      'type': event.event_type,
                      'start': event.started_date.isoformat(),
                      'end': event.ended_date.isoformat()}
            results.append(result)
        return dict(events=results)