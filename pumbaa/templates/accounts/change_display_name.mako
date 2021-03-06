<%inherit file="/base/base_home.mako"/>

<%block name="title">
	Change Username
</%block>

<%block name="where_am_i">
${parent.where_am_i()}
<li><a href="${request.current_route_path()}">Change Password</a></li>
</%block>


<div class="row">
</div>

    <div class="page-header">
        <h1>Edit your profile</h1>
    </div>

    <span class="label label-success"> Current display name : " ${request.user.get_display_name()} "</span><br><br>

    <div class="well">
        <form action="${request.current_route_path()}" method="post">
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
            <div>
        	   <button type="submit" class="btn btn-primary">
                    <span class="glyphicon glyphicon-refresh">
                    </span> Change your profile
                </button>
            </div>
        </form>
    </div>
