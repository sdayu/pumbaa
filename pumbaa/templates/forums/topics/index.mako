<%inherit file="/forums/base/base.mako"/>
<%block name="title">Topics</%block>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
</%block>
<%block name="panel_title">Topics</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('forums.topics.compose')}">new topic</a></li>
</ul>
<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
    </li>
    % endfor
</ul>


