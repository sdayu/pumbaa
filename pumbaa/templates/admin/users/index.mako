<%inherit file="/admin/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.current_route_path()}">Users</a></li>
</%block>
<%block name="panel_title">Users</%block>

<table class="table">
	% for user in users:
    <tr>
    	<td>
    		<b>${user.username}</b> role: ${', '.join([role.name for role in user.roles])}
    	</td>
    	<td>
    		add role: 
    		% for role in models.Role.objects(name__ne='anonymous').all():
    		<a href="${request.route_path('admin.users.add_role', user_id=user.id, role_id=role.id)}">${role.name}</a>
    		% endfor
    	</td>
    </tr>
    % endfor
</table>