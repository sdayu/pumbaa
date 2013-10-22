<%inherit file="/forums/base/base.mako"/>
<%block name="title">List contents by tag: ${tag}</%block>
<%block name="whare_am_i">
${parent.whare_am_i()}
<li><a href="${request.route_path('forums.tags.index')}">Tags</a></li>
</%block>
<%block name="panel_title">Tag: ${tag}</%block>

		<ul class="list-group">
			% for topic in topics:
		    <li class="list-group-item">
		    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
		    </li>
		    % endfor
		</ul>
