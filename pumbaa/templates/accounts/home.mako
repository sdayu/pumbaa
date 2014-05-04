<%inherit file="/base/base_home.mako"/>
<%block name="addition_header">
${parent.addition_header()}
<script type="text/javascript">
if (window.location.hash && window.location.hash === "#_=_") {
    window.location.hash = "";
}
</script>
</%block>
<h1>Hello, ${request.user.username}</h1>
% if request.user.get_profile_picture() is not None:
	${request.user.get_profile_picture() | n}
% endif
% if request.user.status == 'wait for approval':
<b>Your account wait for approval.</b>
% endif

<ul class="list-unstyled">
	<li><b>Default Profile</b>: ${request.user.default_profile}</li>
	<li><b>Roles</b>: ${", ".join([role.name for role in request.user.roles])}</li>
	<li><a href="${request.route_path('accounts.change_display_name')}">change display name</a></li>
	<li><a href="${request.route_path('accounts.change_password')}">change password</a></li>
	<li><a href="${request.route_path('accounts.add_online_account')}">add new profile</a></li>
	<li><a href="${request.route_path('accounts.change_feed_url')}">add your blog</a></li>
</ul>

% if len(request.user.online_profiles) > 0:
<b>Online Profile</b>
<ul class="list-unstyled">
% for profile in request.user.online_profiles:
<li><b>Profile</b>: ${profile.domain}
	<ul>
		<li><b>Display Name:</b> ${profile.display_name}</li>
	</ul>
</li>
% endfor
</ul>
% endif