<%inherit file="/forums/base/base.mako"/>
<%block name="title">Forum</%block>

<%block name="panel_title">Forums</%block>

% for forum in forums:
	<div class="panel panel-info">
  		<div class="panel-heading">
    		<h1 class="panel-title">
    			<a href="${request.route_path('forums.view', name=forum.name)}">${forum.name}</a>
    			<a href="${request.route_path('feeds.forums', forum_name=forum.name)}"><img alt="Atom feed" src="/public/images/feed-icon.svg" width=15px/></a>
    		</h1>
  		</div>
  		<div class="panel-body">
   			<ul class="list-group">
				% for topic in forum.get_topics(10):
			    <li class="list-group-item">
			    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
			    </li>
			    % endfor
			</ul>
  		</div>
	</div>
% endfor
