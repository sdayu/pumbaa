'''
Created on Jun 24, 2014

@author: boatkrap
'''


from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

import datetime
from dateutil import tz, parser

from pumbaa import models

@view_defaults(route_name='apis.events', renderer='json')
class Events:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='apis.events.list', request_method='GET')
    def list_event(self):
        render = self.request.GET.get('render', None)
        event_type = self.request.GET.get('event_type', None)
        started_date_str = self.request.GET.get('start', None)
        ended_date_str = self.request.GET.get('end', None)
        
        if started_date_str:
            started_date = parser.parse(started_date_str)
        else:
            started_date = datetime.datetime.now()
        
        if ended_date_str:
            ended_date = parser.parse(ended_date_str)
        else:
            ended_date = started_date + datetime.timedelta(days=30)
        
        events = models.Event.objects(status='publish', 
                                  started_date__gt=started_date,
                                  ended_date__lt=ended_date)\
                        .order_by('+started_date')

        if event_type:
            events = events.filter(event_type=event_type)
            
        results = []
        ctz = tz.tzlocal()
        for event in events:
            started_date = event.started_date.replace(tzinfo=ctz)
            ended_date = event.ended_date.replace(tzinfo=ctz)
            result = {
                      'id': str(event.id),
                      'title': event.topic.title,
                      'type': event.event_type,
                      'start': started_date.isoformat(),
                      'end': ended_date.isoformat(),
                      'allDay': event.all_day,
                      'url': self.request.route_path('calendars.events.view', event_id=event.id)}
            results.append(result)
        
        if render == 'fullcalendar':
            return results
        
        return dict(events=results)