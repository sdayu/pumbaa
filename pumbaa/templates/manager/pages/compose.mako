<%inherit file="/manager/base/base.mako"/>
<%block name="title">New Pages</%block>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.route_path('manager.pages.index')}">Pages</a></li>
	<li><a href="${request.current_route_path()}">New page</a></li>
</%block>

<%block name="panel_title">New Page</%block>
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
	    % if form.description.errors:
			<span class="text-danger">${form.description.errors[0]}</span>
		% endif
	    ${form.description(class_='form-control', placeholder='Enter description', rows='5')}
	    <p>
	     เขียน description ด้วย <a target="_blank" href="http://en.wikipedia.org/wiki/Markdown">MarkDown</a>
	    </p>
	</div>
	<div class="form-group${' has-error' if form.description.errors else ''}">
	    <label for="tags" class="control-label${' has-error' if form.tags.errors else ''}">Tags</label>
	      % if form.tags.errors:
			<span class="text-danger">${form.tags.errors[0]}</span>
		% endif
	     ${form.tags(class_='form-control', placeholder='Enter tags: pumbaa, CoE, tag')}
	</div>
	<div class="form-group${' has-error' if form.comments_disable.errors else ''}">
	<label class="control-label${' has-error' if form.tags.errors else ''}">Comment:</label>
	 % if form.comments_disable.errors:
		<span class="text-danger">${form.comments_disable.errors[0]}</span>
	% endif
	<br/>
	% for subfield in form.comments_disable:
	<div class="radio-inline">
		${subfield}
		${subfield.label}
	</div>
	% endfor
	</div>
	<div class="form-group">
		<button type="submit" class="btn btn-primary">Submit</button>
	</div>
</form>