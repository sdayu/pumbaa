<%inherit file="/manager/base/base.mako"/>

<%block name="title">New Photo Albums</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.photo_albums.index')}">Photo Albums</a></li>
	<li><a href="${request.current_route_path()}">New page</a></li>
</%block>

<%block name="panel_title">New Photo Albums</%block>
<form action="${request.current_route_path()}" method="post">
	<div class="form-group${' has-error' if form.name.errors else ''}">
	    <label for="title" class="control-label">Name</label>
	    % if form.name.errors:
			<span class="text-danger">${form.name.errors[0]}</span>
		% endif
	    ${form.name(class_='form-control', placeholder='Enter photo album name')}
	</div>
	<div class="form-group${' has-error' if form.description.errors else ''}">
	    <label for="desctiption" class="control-label">Description</label>
	    % if form.description.errors:
			<span class="text-danger">${form.description.errors[0]}</span>
		% endif
	    ${form.description(class_='form-control', placeholder='Enter photo album name')}
	</div>
	<div class="form-group${' has-error' if form.event_date.errors else ''}">
	    <label for="event_date" class="control-label">When</label>
	    % if form.event_date.errors:
			<span class="text-danger">${form.event_date.errors[0]}</span>
		% endif
	    ${form.event_date(class_='form-control', placeholder='yyyy-mm-dd')}
	    <p>เป็น ค.ศ. 2014-03-01</p> 
	</div>
	<div class="checkbox${' has-error' if form.shared.errors else ''}">
	    % if form.shared.errors:
			<span class="text-danger">${form.shared.errors[0]}</span>
		% endif
	    <label for="shared">${form.shared} Allow friends to add photo</label>
	</div>
	<div class="form-group">
		<button type="submit" class="btn btn-primary">Create photo album</button>
	</div>
</form>
