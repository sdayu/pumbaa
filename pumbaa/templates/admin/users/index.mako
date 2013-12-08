<%inherit file="/admin/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Users</a></li>
</%block>
<%block name="panel_title">Users</%block>

total: ${len(users)} users
<table class="table">
	% for user in users:
    <tr>
    	<td>
    		<div class="pull-left" style="margin-right: 3px;">
				${user.get_profile_picture() if user.get_profile_picture() is not None else '' | n}
			</div>
			<div>
	    		<b>${user.username}</b> <br/>
	    		<b>Role:</b> ${', '.join([role.name for role in user.roles])} <br/>
				<b>Approver:</b> ${', '.join([approver.user.get_display_name() for approver in user.approvers])}
    		</div>
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