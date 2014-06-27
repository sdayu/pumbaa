<%inherit file="/forums/base/base.mako"/>
<%! 
	from pyramid.security import has_permission
 %>
 
<%block name="title">${topic.title}</%block>
<%block name="keywords">${", ".join(topic.tags)}</%block>
<%block name="description">${topic.description[:200]}</%block>

<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
</%block>

<%block name="panel_title">
	<h4>${topic.title}
	% if has_permission('topic', request.context, request):
	<span class="pull-right">
		<a href="${request.route_path('manager.topics.change_status', topic_id=topic.id, status='suspend')}" class="btn btn-primary btn-xs">
		<span class="glyphicon glyphicon-stop" title="คุณมีสิทธิ์หยุดเผยแพร่กระทู้"></span>
		</a>
	</span>
	% endif
	</h4>
</%block>
   
<%block name="panel_footer">
	  <div class="panel-footer">
		<p>${'' if topic.author.get_profile_picture() is None else topic.author.get_profile_picture() | n}
		<b>${topic.author.get_display_name()}</b> | ${topic.published_date}</p>
	  </div>
</%block>

<section>
	<article title="topic description" id="description">
${topic.description | n}
	</article>
	<div style="border-top: double #bce8f1; padding-top: 10px;">
		<ul class="list-inline">
			<li>tags:</li>
		% for tag in topic.tags:
			<li><a href="${request.route_path('forums.tags.list_contents', name=tag)}">${tag}</a></li>
		% endfor
		</ul>
	</div>
</section>

<script type="text/javascript">
$( document ).ready(function() {
    $("#description").html(converter.makeHtml($("#description").html()));
});
</script>

<%block name="more_body">
<%include file="/base/social_integration.mako"/>
<%include file="/base/comments.mako" args="item=topic"/>
</%block>
