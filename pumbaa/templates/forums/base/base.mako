<%inherit file="/base/default.mako"/>
<%block name="title">Forums</%block>

<ol class="breadcrumb">
<%block name="where_am_i">
	<li><a href="${request.route_path('forums.index')}">Forums</a></li>
</%block>
</ol>

<div class="panel panel-info">
  <div class="panel-heading">
  	<h1 class="panel-title"><%block name="panel_title">Forums</%block></h1>
  </div>
  <div class="panel-body">

${next.body()}

  </div>
  <%block name="panel_footer"></%block>
</div>

<%block name="more_body"></%block>
