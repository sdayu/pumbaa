<%inherit file="/forums/base/base.mako"/>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
	<li><a href="${request.route_path('calendars.events.index')}">Events</a></li>
</%block>
<%block name="title">Event</%block>
<%block name="panel_title">Event</%block>
