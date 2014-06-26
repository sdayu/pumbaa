<%inherit file="/forums/base/base.mako"/>
<%!
	import json
	from pumbaa.models import events
%>
<%
	def get_color(event_type):
		cmap = {'undergraduate':'#fc9a24',
				'graduate':'#002080',
				'department':'#3366FF',
				'conference':'#FF33CC',
				'thesis':'#1AC6FF',
				'other':'#00B32D'}
		if event_type in cmap:
			return cmap[event_type]
		
		return '#3a87ad'
%>

<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
</%block>
<%block name="title">Calendar</%block>
<%block name="panel_title">Calendar</%block>


<%block name="addition_header">
    <link rel="stylesheet" href="/public/components/fullcalendar/dist/fullcalendar.css">
    <link rel="stylesheet" href="/public/css/calendar_pumbaa.css" />

    <script src="/public/components/jquery-ui/ui/jquery-ui.js"></script>

    <script src="/public/components/angular/angular.js"></script>
    <script src="http://angular-ui.github.io/bootstrap/ui-bootstrap-tpls-0.9.0.js"></script>
    
    <script src="/public/components/moment/min/moment.min.js"></script>
    <script src="/public/components/fullcalendar/dist/fullcalendar.js"></script>
    <script src="/public/components/fullcalendar/dist/gcal.js"></script>
    <script src="/public/components/angular-ui-calendar/src/calendar.js"></script>
    <script src="/public/js/calendar_pumbaa.js"></script>
    
</%block>

<div role="main" ng-app="calendarPumbaaApp" id="top">
        <section id="directives-calendar" ng-controller="CalendarCtrl" data-ng-init="init(${json.dumps([dict(name=type, color=get_color(type)) for type in events.EVENT_TYPES])})">
                <div class="rows" >
                	<div class="col-sm-3">
                		<div class="btn-group-vertical">
                		% for t in events.EVENT_TYPES:
                		<button class="btn btn-default" ng-click="addRemoveEventSource(eventSources, pumbaaSources['${t}'])">
                            ${t.title()}
                        </button>
                		% endfor
                		<button class="btn btn-default" ng-click="addRemoveEventSource(eventSources, holidaySource)">
                            Holiday
                        </button>
                		</div>
                	</div>
                    <div class="col-sm-9">
                              <div class="alert-success calAlert" ng-show="alertMessage != undefined && alertMessage != ''">
                                <h4>{{alertMessage}}</h4>
                              </div>
                              <div class="btn-toolbar">
                                <div class="btn-group">
                                    <button class="btn btn-success" ng-click="changeView('agendaDay', pumbaaCalendar)">AgendaDay</button>
                                    <button class="btn btn-success" ng-click="changeView('agendaWeek', pumbaaCalendar)">AgendaWeek</button>
                                    <button class="btn btn-success" ng-click="changeView('month', pumbaaCalendar)">Month</button>
                                </div>
                              </div>
                            <div class="calendar" ng-model="eventSources" calendar="pumbaaCalendar" config="uiConfig.calendar" ui-calendar="uiConfig.calendar"></div>
                    </div>
                </div>
        </section>
</div>