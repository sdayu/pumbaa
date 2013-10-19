<%inherit file="/forums/base/base.mako"/>
<%block name="title">${topic.title}</%block>
<%block name="whare_am_i">
	${parent.whare_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
</%block>
<%block name="panel_title">${topic.title}</%block>
   
<%block name="panel_footer">
	  <div class="panel-footer">
	  	tags:
	  		<ul class="list-inline">
	 		% for tag in topic.tags:
	 			<li><a href="${request.route_path('forums.tags.list_contents', name=tag)}">${tag}</a></li>
	 		% endfor
	 		</ul>
	  	</div>
</%block>	  	

${topic.description}

<%block name="more_body">
<section title="do-comments">
	<form action="${request.route_path('forums.comments.comment', topic_id=topic.id)}" method="post">
		<div class="form-group">
		    <label for="comment">Comment</label>
		    <textarea name="message" rows="5" class="form-control" placeholder="Put your comment"></textarea>
		</div>
		<button type="submit">Submit</button>
	</form>
</section>

<section title="comments" style="margin-top: 10px;">
% for comment in topic.comments:
	<div class="well">
		<p>${comment.message}</p>
		<p><b>${comment.author.username}</b> | ${comment.published_date}</p>
	</div>
% endfor
</section>
</%block>