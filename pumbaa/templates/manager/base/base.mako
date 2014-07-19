<%inherit file="/base/base_home.mako"/>
<%block name="title">Manager</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	% if request.route_path('manager.index') == request.current_route_path():
	<li class="active">Manager</li>
	% else:
	<li><a href="${request.route_path('manager.index')}">Manager</a></li>
	% endif
</%block>

<div class="panel panel-info">
  <div class="panel-heading">
  	<h1 class="panel-title"><%block name="panel_title">Manager</%block></h1>
  </div>
  <div class="panel-body">

${next.body()}

  </div>
</div>
