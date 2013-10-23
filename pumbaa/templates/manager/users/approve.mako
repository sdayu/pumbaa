<%inherit file="/manager/base/base.mako"/>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Approve user list</a></li>
</%block>
<%block name="panel_title">Approve user list</%block>
<ul>
	% if len(users) == 0:
	There are no waiting user for approval.
	% endif
	% for user in users:
	<li>${user.username} 
		<ul>
			<li>profile: ${user.default_profile}</li>
			<li>name: ${user.first_name} ${user.last_name}</li>
		% if len(user.approvers) > 0:
		<li><i>approvers:</i> 
		% for approver in user.approvers:
			${approver.user.username} 
		% endfor
		</li>
		% endif
	 		<li><a href="${request.route_path('manager.users.do_approve', user_id=user.id)}">approve</a></li>
	 	</ul>
	 </li>
	% endfor
</ul>