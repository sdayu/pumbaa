<%inherit file="/forums/base/base.mako"/>
<%block name="where_am_i">
	<li><a href="${request.route_path('calendars.calendars.index')}">Calendars</a></li>
	<li><a href="${request.route_path('calendars.events.index')}">Events</a></li>
	<li><a href="${request.current_route_path()}">${event.topic.title}</a></li>
</%block>
<%block name="title">Event: ${event.topic.title}</%block>
<%block name="keywords">${", ".join(event.topic.tags)}</%block>
<%block name="description">${event.topic.description[:200]}</%block>

<%block name="panel_title">
	<h4>Event: ${event.topic.title}</h4>
</%block>

<%block name="panel_footer">
	  <div class="panel-footer">
		<p>${'' if event.author.get_profile_picture() is None else topic.author.get_profile_picture() | n}
		<b>${event.author.get_display_name()}</b> | ${event.topic.published_date}</p>
	  </div>
</%block>

<section>
	<div>
		<b>Title:</b> ${event.topic.title}
	</div>
	<div>
		<b>Description:</b> <br/>
                <div class="well">
		<article title="topic description" id="description">
${event.topic.description}
		</article>
                </div>
	</div>
	<div>
		<b>Started date:</b> ${event.started_date.strftime('%a %d %b %Y %H:%M')}
	</div>
	<div>
		<b>Ended date:</b> ${event.ended_date.strftime('%a %d %b %Y %H:%M')}
	</div>
	% if event.event_type == 'conference':
	% if event.conference.paper_deadline_date:
	<div>
		<b>Paper deadline:</b> <span style="color: red; font-weight: bold;">${event.conference.paper_deadline_date.strftime('%a %d %b %Y')}</span>
	</div>
	% endif
	% if event.conference.notification_date:
	<div>
		<b>Notification date:</b> ${event.conference.notification_date.strftime('%a %d %b %Y')}
	</div>
	% endif
	% endif
	<div>
		<b>Where:</b> ${event.venue if event.venue else ''}
	</div>
	<div>
		<b>Tags:</b> 
		% for tag in event.topic.tags:
			<a href="${request.route_path('calendars.events.list_by_tags', name=tag)}">${tag}</a>,
		% endfor
	</div>
</section>

<script type="text/javascript">
$( document ).ready(function() {
    $("#description").html(converter.makeHtml($("#description").html()));
});
</script>

<%block name="more_body">
<%include file="/base/social_integration.mako"/>
<%include file="/base/comments.mako" args="item=event.topic"/>
</%block>
