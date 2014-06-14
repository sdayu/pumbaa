<%inherit file="/manager/base/base.mako"/>
<%block name="title">Calendars</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Events</a></li>
</%block>
<%block name="panel_title">Events</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('manager.events.add')}">New Event</a></li>
</ul>
<ul class="list-group">
	% for event in events:
    <li class="list-group-item">
    	<a href="${request.route_path('calendars.events.view', event_id=event.id)}">${event.topic.title}</a>
    </li>
    % endfor
</ul>
