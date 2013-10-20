<%inherit file="/admin/base/base.mako"/>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.current_route_path()}">Forums</a></li>
</%block>
<%block name="panel_title">New Forums</%block>
<form action="${request.current_route_path()}" method="post" role="form">
			% for field in form:
				<% css_class = 'form-group' %>
		    	% if field.errors:
		    	<% css_class += ' has-error' %>
		    	% endif
		    <div class="${css_class}">
		    	${field.label(class_="control-label")}
		    	% if field.errors:
		    	<span class="text-danger">${field.errors[0]}</span>
		    	% elif field.flags.required:
		    	<span style="color: red;">*</span>
		    	% endif
		    	${field(class_='form-control', placeholder='Enter '+field.label.text.lower())}
		  	</div>
			% endfor
			<button type="submit" class="btn btn-primary">สร้าง</button>
		</form>
