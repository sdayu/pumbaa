<%inherit file="/manager/base/base.mako"/>
<%block name="title">Administrator</%block>
<%block name="whare_am_i">
	<li><a href="${request.route_path('admin.index')}">Administrator</a></li>
</%block>
<%block name="panel_title">Administrator</%block>
${next.body()}