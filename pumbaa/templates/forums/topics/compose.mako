<%inherit file="/forums/base/base.mako"/>
<%block name="title">New Topic</%block>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
</%block>

<%block name="panel_title">New Topic</%block>
<form action="${request.current_route_path()}" method="post">
	<div class="form-group${' has-error' if form.title.errors else ''}">
	    <label for="title" class="control-label${' has-error' if form.title.errors else ''}">Title</label>
	    % if form.title.errors:
			<span class="text-danger">${form.title.errors[0]}</span>
		% endif
	    ${form.title(class_='form-control', placeholder='Enter title')}
	</div>
	<div class="form-group${' has-error' if form.description.errors else ''}">
	    <label for="description" class="control-label${' has-error' if form.description.errors else ''}">Description</label>
	    ${form.description(class_='form-control', placeholder='Enter description', rows='5')}
	</div>
	<div class="form-group${' has-error' if form.description.errors else ''}">
	    <label for="tags" class="control-label${' has-error' if form.tags.errors else ''}">Tags</label>
	     ${form.tags(class_='form-control', placeholder='Enter tags: pumbaa, CoE, tag')}
	</div>
	<button type="submit" class="btn btn-primary">Submit</button>
</form>