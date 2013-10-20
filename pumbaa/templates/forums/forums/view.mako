<%inherit file="/forums/base/base.mako"/>
<%block name="title">${forum.name}</%block>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.route_path('forums.view', name=forum.name)}">${forum.name}</a></li>
</%block>
<%block name="panel_title">
	${forum.name} 
	<a href="${request.route_path('feeds.forums', forum_name=forum.name)}">
		<img alt="Atom feed" src="/public/images/feed-icon.svg" width=15px/>
	</a>
</%block>

<div class="well">
${forum.description}
</div>

<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
    </li>
    % endfor
</ul>
