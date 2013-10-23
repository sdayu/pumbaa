<%inherit file="/base/default.mako"/>
<%!
	from velruse import login_url
%>
<%block name="addition_header">
<style type="text/css">
.form-register {
  max-width: 500px;
  margin: 0 auto;
}
.slogo{	
        text-decoration:none;
		padding: 4px;}
	.slogo:hover { background:#0099FF;}
	.slogo:hover img{ visibility:hidden;}
</style>
</%block>
<h1>ลงทะเบียน</h1>
<div class="row">
	<div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
		<form action="${request.current_route_path()}" method="post" role="form" class="form-register">
			% for field in form:
				% if field.type == 'BooleanField':
				<% continue %>
				% endif
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
			<label class="checkbox">
		    	${form.agree_term} You agree to our terms
		  	</label>
			<button type="submit" class="btn btn-primary">ลงทะเบียน</button>
		</form>
	</div>
	<div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">
		<h3>Register with</h3>
		<ul class="list-inline">
			<li><a href="${login_url(request, 'facebook')}"><img src="/public/images/f.png" width="70px" class="slogo"/></a></li>
			<li><a href="${login_url(request, 'google')}"><img src="/public/images/g.png" width="70px" class="slogo"/></a></li>
			<li><a href="${login_url(request, 'twitter')}"><img src="/public/images/t.png" width="70px" class="slogo"/></a></li>
		</ul>
	</div>
</div>