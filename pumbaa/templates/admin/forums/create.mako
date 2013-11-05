<%inherit file="/admin/base/base.mako"/>
<%block name="addition_header">
	<link rel="stylesheet" type="text/css" href="/public/libs/select2/3.4.2/select2.css" />
	<script type="text/javascript" src="/public/libs/select2/3.4.2/select2.js"></script>
</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
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
		    	% if field.type == 'HiddenField':
		    	${field(style="width:100%")}
		    	% else: 
		    	${field(class_='form-control', placeholder='Enter '+field.label.text.lower())}
		    	% endif
		  	</div>
			% endfor
			<button type="submit" class="btn btn-primary">สร้าง</button>
		</form>
		
## select2
<script type="text/javascript">
$("#tags").select2({
    tags:${tags | n},
    placeholder: "Enter tags: pumbaa, CoE, tag",
    tokenSeparators: [","],
    maximumInputLength: 30
});
</script>