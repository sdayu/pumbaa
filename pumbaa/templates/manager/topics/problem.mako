<%inherit file="/manager/base/base.mako"/>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.topics.index')}">Topic</a></li>
	<li><a href="#">Problem</a></li>
</%block>
<%block name="panel_title">Topics Problem</%block>
<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a> |
    	<a href="${request.route_path('manager.topics.change_status', topic_id=topic.id, status='publish')}">publish</a>
    	<a href="${request.route_path('manager.topics.change_status', topic_id=topic.id, status='delete')}">delete</a>
    </li>
    % endfor
</ul>