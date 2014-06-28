<%inherit file="/forums/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
	<li><a href="${request.route_path('calendars.events.index')}">Events</a></li>
</%block>
<%block name="title">Event</%block>
<%block name="panel_title">Event</%block>
	  	<ul class="list-inline">
	    % for tag in tags:
	   		<li style="padding: 2px;">
	   			<a href="${request.route_path('calendars.events.list_by_tags', name=tag)}" class="btn btn-default btn-sm">
	   				${tag} 
	   				<span class="badge">${models.Topic.objects(tags=tag, type='event').count()}</span>
				</a>
	   		</li>
	    % endfor
	    </ul>
