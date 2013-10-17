<%inherit file="/base/base.mako"/>
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
		<div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">
			<nav>
				<ul class="nav bs-sidenav">
					<li class="active">
						<a href="${request.route_path('manager.users.approve')}">Approve user</a>
					</li>
					<li>
						<a href="#">Topic</a>
					</li>
				</ul>
			</nav>
		</div>
		<div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
			## whare am i bar
			<nav>
				<ol class="breadcrumb">
				  <li><a href="${request.route_path('home')}">Home</a></li>
				  <%block name="whare_am_i"></%block>
				</ol>
			</nav>
			
			${next.body()}
		</div>
	</div>
</div>

