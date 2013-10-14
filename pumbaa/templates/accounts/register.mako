<%inherit file="/base/default.mako"/>
<%block name="addition_header">
<style type="text/css">
.form-register {
  max-width: 500px;
  margin: 0 auto;
}
</style>
</%block>
<h1>ลงทะเบียน</h1>
<form action="${request.current_route_path()}" method="post" role="form" class="form-register">
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
	<button type="submit" class="btn btn-primary">ลงทะเบียน</button>
</form>