<%inherit file="/forums/base/base.mako"/>
<%block name="title">Pages</%block>
<%block name="where_am_i">
	<li class="active">Pages</li>
</%block>
<%block name="panel_title">Pages</%block>

<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('pages.view', title=topic.title)}">${topic.title}</a>
    </li>
    % endfor
</ul>


