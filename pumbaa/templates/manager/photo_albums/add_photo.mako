<%inherit file="/manager/base/base.mako"/>

<%block name="title">New Photo Albums</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.pages.index')}">Photo Albums</a></li>
	<li><a href="${request.current_route_path()}">New photo</a></li>
</%block>

<%block name="panel_title">New Photo</%block>
<form action="${request.current_route_path()}" method="post" accept-charset="utf-8" enctype="multipart/form-data">
	<div class="form-group${' has-error' if form.image.errors else ''}">
	    <label for="title" class="control-label${' has-error' if form.image.errors else ''}">Photo</label>
	    % if form.image.errors:
			<span class="text-danger">${form.image.errors[0]}</span>
		% endif
	    ${form.image(class_='form-control')}
	</div>
	<div class="form-group">
		<button type="submit" class="btn btn-primary">Add photo</button>
	</div>
</form>
