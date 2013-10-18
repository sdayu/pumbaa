<%inherit file="/base/base_home.mako"/>
<%block name="title">Forums</%block>
<%block name="whare_am_i"><li><a href="${request.route_path('forums.index')}">Forums</a></li></%block>

<div class="panel panel-default">
  <div class="panel-heading">
  	<h1 class="panel-title"><%block name="panel_title">Forums</%block></h1>
  </div>
  <div class="panel-body">

${next.body()}

  </div>
</div>
