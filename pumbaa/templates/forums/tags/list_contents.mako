<%inherit file="/base/default.mako"/>
<%block name="title">List contents by tag: ${tag}</%block>

<section title="topic">
	<div class="panel panel-info">
	  <div class="panel-heading">
	    <h1 class="panel-title">Tag: ${tag}</h1>
	  </div>
	  <div class="panel-body">
		<ul class="list-group">
			% for topic in topics:
		    <li class="list-group-item">
		    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
		    </li>
		    % endfor
		</ul>
	</div>
</section>