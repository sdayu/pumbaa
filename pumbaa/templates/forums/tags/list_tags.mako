<%inherit file="/base/default.mako"/>
<%block name="title">List all tags</%block>

<section title="topic">
	<div class="panel panel-info">
	  <div class="panel-heading">
	    <h1 class="panel-title">Tags</h1>
	  </div>
	  <div class="panel-body">
	  	<ul class="list-inline">
	    % for tag in tags:
	   		<li><a href="${request.route_path('forums.tags.list_contents', name=tag)}">${tag}</a></li>
	    % endfor
	    </ul>
	  </div>
	</div>
</section>