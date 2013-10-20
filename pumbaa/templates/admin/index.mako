<%inherit file="/admin/base/base.mako"/>

<ul>
	<li><a href="${request.route_path('admin.forums.index')}">Forum manager</a></li>
	<li><a href="${request.route_path('admin.users.index')}">User manager</a></li>
</ul>