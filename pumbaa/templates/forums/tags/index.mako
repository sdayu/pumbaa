<%inherit file="/forums/base/base.mako"/>
<%block name="title">List all tags</%block>
<%block name="whare_am_i">
${parent.whare_am_i()}
<li><a href="${request.route_path('forums.tags.index')}">Tags</a></li>
</%block>
<%block name="panel_title">All tags</%block>

	  	<ul class="list-inline">
	    % for tag in tags:
	   		<li><a href="${request.route_path('forums.tags.list_contents', name=tag)}">${tag}</a></li>
	    % endfor
	    </ul>
