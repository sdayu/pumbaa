<%inherit file="/forums/base/base.mako"/>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
	<li><a href="${request.route_path('calendars.events.index')}">Events</a></li>
	<li><a href="${request.current_route_path()}">${event.topic.title}</a></li>
</%block>
<%block name="title">Event: ${event.topic.title}</%block>
<%block name="panel_title">Event: ${event.topic.title}</%block>
<p>
	<b>Title:</b> ${event.topic.title}
</p>
<p>
	<b>Description:</b> ${event.topic.description}
</p>
<p>
	<b>Started date:</b> ${event.started_date.strftime('%a %d %b %Y %H:%M')}
</p>
<p>
	<b>Ended date:</b> ${event.ended_date.strftime('%a %d %b %Y %H:%M')}
</p>
<p>
	<b>Where:</b> ${event.venue if event.venue else ''}
</p>
<p>
	<b>Tags:</b> ${', '.join(event.topic.tags)}
</p>
