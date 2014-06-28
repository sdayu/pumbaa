<%inherit file="/forums/base/base.mako"/>
<%block name="title">List events by tag: ${tag}</%block>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
	<li><a href="${request.route_path('calendars.events.index')}">Events</a></li>
	<li><a href="${request.current_route_path()}">${tag}</a></li>
</%block>
<%block name="panel_title">Tag: ${tag}</%block>

		<ul class="list-group">
			% for event in events:
		    <li class="list-group-item">
		    	<a href="${request.route_path('calendars.events.view', event_id=event.id)}">
		    		${event.topic.title} : 
		    		started ${event.started_date}
		    	</a>
		    </li>
		    % endfor
		</ul>
