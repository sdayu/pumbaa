<%inherit file="/base/base_home.mako"/>

<ul>
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