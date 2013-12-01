<%inherit file="/base/base_home.mako"/>
<%!
	from velruse import login_url
%>

<%block name="addition_header">
${parent.addition_header()}
</%block>

<%block name="title">Add other online account</%block>

<h1>Add other online account</h1>
% if request.user.get_profile_picture() is not None:
	${request.user.get_profile_picture() | n}
% endif


% if len(request.user.online_profiles) > 0:
<b>Online Profile</b>
<ul class="list-unstyled">
% for profile in request.user.online_profiles:
<li><b>Profile</b>: ${profile.domain}
	<ul>
		<li><b>Display Name:</b> profile.display_name</li>
	</ul>
</li>
% endfor
</ul>
% endif

<ul class="list-inline">
	<li><a href="${login_url(request, 'facebook')}"><img src="/public/images/f.png" width="70px" class="slogo"/></a></li>
	<li><a href="${login_url(request, 'google')}"><img src="/public/images/g.png" width="70px" class="slogo"/></a></li>
	<li><a href="${login_url(request, 'twitter')}"><img src="/public/images/t.png" width="70px" class="slogo"/></a></li>
</ul>