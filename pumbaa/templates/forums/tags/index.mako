<%inherit file="/forums/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="title">List all tags</%block>
<%block name="whare_am_i">
${parent.whare_am_i()}
<li><a href="${request.route_path('forums.tags.index')}">Tags</a></li>
</%block>
<%block name="panel_title">All tags</%block>

	  	<ul class="list-inline">
	    % for tag in tags:
	   		<li>
	   			<a href="${request.route_path('forums.tags.list_contents', name=tag)}">
	   				${tag} 
	   				<span class="badge">${models.Topic.objects(tags=tag).count()}</span>
				</a>
	   		</li>
	    % endfor
	    </ul>
