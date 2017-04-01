<%inherit file="/manager/base/base.mako"/>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Pages</a></li>
</%block>
<%block name="panel_title">Pages</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('manager.pages.compose')}">new pages</a></li>
</ul>
<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('pages.view', title=topic.title)}">${topic.title}</a> ::
    	<a href="${request.route_path('manager.pages.edit', topic_id=topic.id)}">Edit</a>
    </li>
    % endfor
</ul>