<%inherit file="/base/base.mako"/>
<%! from pyramid.security import has_permission %>
<%block name="addition_header">
<style type="text/css">
.bs-sidenav {
    margin-top: 30px;
    margin-bottom: 30px;
    padding-top: 10px;
    padding-bottom: 10px;
    text-shadow: 0px 1px 0px rgb(255, 255, 255);
    background-color: rgb(247, 245, 250);
    border-radius: 5px 5px 5px 5px;
}
</style>
</%block>
<%include file="/base/navigator_bar.mako"/>
<div style="padding: 30px;"></div>
<div class="container">
	<div class="row">
		<div class="col-xs-4 col-sm-4 col-md-3 col-lg-3">
			<nav>
				<div class="list-group panel-primary">
					<a class="list-group-item" class="active" href="${request.route_path('manager.users.approve')}">Approve users</a>
					<a class="list-group-item" href="${request.route_path('manager.topics.index')}">Topic</a>
					<a class="list-group-item" href="${request.route_path('manager.photo_albums.index')}">Photo Albums</a>
					<a class="list-group-item" href="${request.route_path('manager.events.index')}">Events</a>
					% if has_permission('topic', request.context, request):
					<a class="list-group-item" href="${request.route_path('manager.topics.problem')}">Topic Problem</a>
					% endif
					% if has_permission('page', request.context, request):
					<a class="list-group-item" href="${request.route_path('manager.pages.index')}">Pages</a>
					% endif
					% if has_permission('admin', request.context, request):
					<a class="list-group-item" href="${request.route_path('admin.index')}">admin</a>
					% endif
				</div>
			</nav>
		</div>
		<div class="col-xs-8 col-sm-8 col-md-9 col-lg-9">
			## whare am i bar
			<section title="where am i bar">
				<ol class="breadcrumb">
				  <%block name="where_am_i">
				  <li style="margin-left:-25px;"><a href="${request.route_path('home')}"><i class="glyphicon glyphicon-home"></i></a></li>
				  </%block>
				</ol>
			</section>
			
			${next.body()}
		</div>
	</div>
</div>

