<%inherit file="/manager/base/base.mako"/>
<%block name="title">Calendars</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li class="active">Events</li>
</%block>
<%block name="panel_title">Events</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('manager.events.create')}">New Event</a></li>
</ul>
<ul class="list-group">
	% for event in events:
    <li class="list-group-item">
    	<a href="${request.route_path('calendars.events.view', event_id=event.id)}">${event.topic.title}</a>
    	<div class="pull-right">
    		<a href="${request.route_path('manager.events.edit', event_id=event.id)}">
    			 <span class="glyphicon glyphicon-edit"></span>
    		</a>
    		<a href="${request.route_path('manager.events.delete', event_id=event.id)}">
    			<span class="glyphicon glyphicon-remove"></span>
    		</a>
    	</div>
    </li>
    % endfor
</ul>
