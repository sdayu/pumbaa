<%inherit file="/forums/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="title">List all tags</%block>
<%block name="where_am_i">
${parent.where_am_i()}
<li class="active">Tags</li>
</%block>
<%block name="panel_title">All tags</%block>

	  	<ul class="list-inline">
	    % for tag in tags:
	   		<li style="padding: 2px;">
	   			<a href="${request.route_path('forums.tags.list_contents', name=tag)}" class="btn btn-default btn-sm">
	   				${tag} 
	   				<span class="badge">${models.Topic.objects(tags=tag).count()}</span>
				</a>
	   		</li>
	    % endfor
	    </ul>
