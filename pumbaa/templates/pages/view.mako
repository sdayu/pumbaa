<%inherit file="/forums/topics/view.mako"/>
<%block name="where_am_i">
	<li><a href="${request.route_path('pages.index')}">Pages</a></li>
	<li class="active">${topic.title.title()}</li>
</%block>
