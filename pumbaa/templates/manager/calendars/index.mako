<%inherit file="/manager/base/base.mako"/>
<%block name="title">Calendars</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Calendars</a></li>
</%block>
<%block name="panel_title">Calendars</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('manager.calendars.add')}">New Event</a></li>
</ul>
<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
    </li>
    % endfor
</ul>
