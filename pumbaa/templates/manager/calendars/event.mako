<%inherit file="/manager/base/base.mako"/>
<%block name="title">Calendars</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.calendars.index')}">Calendars</a></li>
	<li><a href="${request.current_route_path()}">Create Event</a></li>
</%block>
<%block name="panel_title">Create Calendars</%block>
<form action="${request.current_route_path()}" method="post" accept-charset="utf-8">
	<div class="form-group${' has-error' if form.title.errors else ''}">
	    <label class="control-label">Title</label>
		% if form.title.errors:
			<span class="text-danger">${form.title.errors[0]}</span>
		% endif
		${form.title(class_='form-control')}
	</div>	
	<div class="form-group${' has-error' if form.description.errors else ''}">
	    <label class="control-label">Description</label>
		% if form.description.errors:
			<span class="text-danger">${form.description.errors[0]}</span>
		% endif
		${form.title(class_='form-control')}
	</div>
	<div class="row">
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.started_date.errors else ''}">
				<label class="control-label">From</label>
				% if form.description.errors:
					<span class="text-danger">${form.started_date.errors[0]}</span>
				% endif
				${form.started_date(class_='form-control')}
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.ended_date.errors else ''}">
				<label class="control-label">To</label>
				% if form.ended_date.errors:
					<span class="text-danger">${form.ended_date.errors[0]}</span>
				% endif
				${form.ended_date(class_='form-control')}
			</div>
		</div>
	</div>
	
	<label class="checkbox-inline">
		${form.all_day} All day
	</label>
	<label class="checkbox-inline">
		${form.repeat} Repeat
	</label>
	<div class="form-group${' has-error' if form.event_type.errors else ''}">
	    <label class="control-label">Event Type</label>
		% if form.event_type.errors:
			<span class="text-danger">${form.event_type.errors[0]}</span>
		% endif
		${form.event_type(class_='form-control')}
	</div>
	<div class="form-group${' has-error' if form.place.errors else ''}">
	    <label class="control-label">Where</label>
		% if form.place.errors:
			<span class="text-danger">${form.place.errors[0]}</span>
		% endif
		${form.place(class_='form-control')}
	</div>
	<div class="form-group${' has-error' if form.tags.errors else ''}">
	    <label class="control-label">Tags</label>
		% if form.tags.errors:
			<span class="text-danger">${form.tags.errors[0]}</span>
		% endif
		${form.tags(class_='form-control')}
	</div>
	
</form>