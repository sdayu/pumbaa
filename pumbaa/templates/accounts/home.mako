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
<li><b>Roles</b>: ${", ".join([role.name for role in request.user.roles])}</li>
<li><a href="${request.route_path('accounts.change_username')}">change username</a></li>
<li><a href="${request.route_path('accounts.change_password')}">change password</a></li>
</ul>