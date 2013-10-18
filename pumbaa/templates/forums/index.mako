<%inherit file="/forums/base/base.mako"/>
<%block name="title">Title</%block>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
</%block>

<%block name="panel_title">Topics</%block>