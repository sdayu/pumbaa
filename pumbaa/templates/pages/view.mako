<%inherit file="/forums/topics/view.mako"/>
<%block name="where_am_i">
	<li><a href="${request.route_path('pages.index')}">Pages</a></li>
	<li><a href="${request.current_route_path()}">${topic.title}</a></li>
</%block>
