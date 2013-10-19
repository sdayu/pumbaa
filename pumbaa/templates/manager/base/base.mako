<%inherit file="/base/base_home.mako"/>
<%block name="title">Manager</%block>
<%block name="whare_am_i"><li><a href="${request.route_path('manager.index')}">Manager</a></li></%block>

<div class="panel panel-info">
  <div class="panel-heading">
  	<h1 class="panel-title"><%block name="panel_title">Manager</%block></h1>
  </div>
  <div class="panel-body">

${next.body()}

  </div>
</div>
