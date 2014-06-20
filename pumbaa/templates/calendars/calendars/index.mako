<%inherit file="/forums/base/base.mako"/>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
</%block>
<%block name="title">Calendar</%block>
<%block name="panel_title">Calendar</%block>
