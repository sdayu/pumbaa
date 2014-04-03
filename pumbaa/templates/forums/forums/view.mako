<%inherit file="/forums/base/base.mako"/>
<%block name="keywords">${", ".join(forum.tags)}</%block>
<%block name="description">${forum.description[:200]}</%block>

<%block name="title">${forum.name}</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('forums.view', name=forum.name)}">${forum.name}</a></li>
</%block>
<%block name="panel_title">
	${forum.name} 
	<a href="${request.route_path('forums.feeds.forums', forum_name=forum.name)}">
		<img alt="Atom feed" src="/public/images/feed-icon.svg" width=15px/>
	</a>
</%block>

<div class="well">
<p>${forum.description}</p>
<p><b>process tags</b>: ${", ".join([tag for tag in forum.tags])}</p>
</div>

<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
    </li>
    % endfor
</ul>
<%include file="/base/pagination.mako" args="page=page,pages=pages"/>