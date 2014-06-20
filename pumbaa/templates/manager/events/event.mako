<%inherit file="/manager/base/base.mako"/>

<%block name="addition_header">
	<link rel="stylesheet" type="text/css" href="/public/libs/select2/3.4.8/select2.css" />
	<link rel="stylesheet" type="text/css" href="/public/libs/select2/3.4.8/select2-bootstrap.css" />
	<script type="text/javascript" src="/public/libs/select2/3.4.8/select2.js"></script>
	
	<script type="text/javascript" src="/public/libs/moment/2.6.0/moment.min.js"></script>
	<link rel="stylesheet" type="text/css" href="/public/libs/bootstrap/plugins/datetimepicker/3.0.0/css/bootstrap-datetimepicker.min.css" />
	<script type="text/javascript" src="/public/libs/bootstrap/plugins/datetimepicker/3.0.0/js/bootstrap-datetimepicker.min.js"></script>
	
	<script>
	$(document).ready(function(){
		$("#tags").select2({
		    tags:${tags | n},
		    placeholder: "Enter tags: pumbaa, CoE, tag",
		    tokenSeparators: [","],
		    maximumInputLength: 30
		});
		
		$(function () {
            $('#started_date_picker').datetimepicker();
            $('#updated_date_picker').datetimepicker();
        });
	});
	</script>
</%block>

<%block name="title">Events</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.events.index')}">Events</a></li>
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
		${form.description(class_='form-control')}
	</div>
	<div class="row">
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.started_date.errors else ''}">
				<label class="control-label">From</label>
				% if form.started_date.errors:
					<span class="text-danger">${form.started_date.errors[0]}</span>
				% endif
				<div class='input-group date' id='started_date_picker' data-date-format="DD/MM/YYYY HH:mm">
					${form.started_date(class_='form-control')}
					<span class="input-group-addon">
						<span class="glyphicon glyphicon-time"></span>
					</span>
				</div>
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.ended_date.errors else ''}">
				<label class="control-label">To</label>
				% if form.ended_date.errors:
					<span class="text-danger">${form.ended_date.errors[0]}</span>
				% endif
				<div class='input-group date' id='updated_date_picker' data-date-format="DD/MM/YYYY HH:mm">
					${form.ended_date(class_='form-control')}
					<span class="input-group-addon">
						<span class="glyphicon glyphicon-time"></span>
					</span>
				</div>
			</div>
		</div>
	</div>
	
	<label class="checkbox-inline">
		${form.all_day} All day
	</label>
	<label class="checkbox-inline">
		## ${form.repeat} Repeat
	</label>
	<div class="form-group${' has-error' if form.event_type.errors else ''}">
	    <label class="control-label">Event Type</label>
		% if form.event_type.errors:
			<span class="text-danger">${form.event_type.errors[0]}</span>
		% endif
		${form.event_type(class_='form-control')}
	</div>
	<div class="form-group${' has-error' if form.venue.errors else ''}">
	    <label class="control-label">Where</label>
		% if form.venue.errors:
			<span class="text-danger">${form.venue.errors[0]}</span>
		% endif
		${form.venue(class_='form-control')}
	</div>
	<div class="form-group${' has-error' if form.tags.errors else ''}">
	    <label class="control-label">Tags</label>
		% if form.tags.errors:
			<span class="text-danger">${form.tags.errors[0]}</span>
		% endif
		<br/>
		${form.tags(class_='form-control', placeholder='Add tags')}
		
	</div>
	<button type="submit" class="btn btn-primary">Add new event</button>
	
</form>