<%inherit file="/forums/base/base.mako"/>

<%block name="keywords">${", ".join(set([", ".join(topic.tags) for topic in topics[:10]]))}</%block>
<%block name="description">${"There are many topics as follow: " + ", ".join(topic.title for topic in topics[:10])}</%block>

<%block name="title">Topics</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li class="active">Topics</li>
</%block>
<%block name="panel_title">Topics</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('forums.topics.compose')}"><b>New Topic</b></a></li>
</ul>
<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
    </li>
    % endfor
</ul>
<%include file="/base/pagination.mako" args="page=page,pages=pages"/>
