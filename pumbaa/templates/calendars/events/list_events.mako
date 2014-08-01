<%inherit file="/forums/base/base.mako"/>
<%!
	import datetime
%>
<%block name="title">List events by tag: ${tag}</%block>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
	<li><a href="${request.route_path('calendars.events.index')}">Events</a></li>
	<li class="active">${tag}</li>
</%block>
<%block name="panel_title">Tag: ${tag}</%block>

		<div class="list-group">
			% for event in events:
			<% 
	  			style=''
	  			if event.started_date.date() <= datetime.datetime.now().date():
	  				style = ' list-group-item-success'
	  			elif event.started_date.date() == datetime.datetime.now().date() + datetime.timedelta(days=1):
	  				style = ' list-group-item-warning'
	  			elif event.ended_date.date() < datetime.datetime.now().date():
	  				style = ' list-group-item-danger'
	  		%>
		    
	    	<a href="${request.route_path('calendars.events.view', event_id=event.id)}" class="list-group-item${style}">
	    		<div class="row">
		    		<div class="col-sm-2">
		    			${event.started_date.date()}
		    		</div>
	    			<div class="col-sm-10">
		  				<section>
		  				<h4 class="list-group-item-heading">${event.topic.title}</h4>
						% if event.all_day:
							<i>${event.started_date.date()} - ${event.ended_date.date()}</i>
							% else:
							<i>${event.started_date} - ${event.ended_date}</i>
							% endif
							<br/>
						% if event.venue:
						<b>where:</b> ${event.venue}<br/>
						% endif
		  				</section>
		  			</div>
  				</div>
	    	</a>
		    
		    % endfor
		</div>
