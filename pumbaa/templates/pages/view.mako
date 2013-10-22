<%inherit file="/forums/base/base.mako"/>
<%! import markdown %>
<%block name="title">${topic.title}</%block>
<%block name="where_am_i">
	<li><a href="${request.route_path('pages.index')}">Pages</a></li>
	<li><a href="${request.current_route_path()}">${topic.title}</a></li>
</%block>
<%block name="panel_title">${topic.title}</%block>
   
<%block name="panel_footer">
	  <div class="panel-footer">
	  		<ul class="list-inline">
	  			<li>tags:</li>
	 		% for tag in topic.tags:
	 			<li><a href="${request.route_path('forums.tags.list_contents', name=tag)}">${tag}</a></li>
	 		% endfor
	 		</ul>
	  	</div>
</%block>	  	

<section title="topic description">
${markdown.markdown(topic.description) | n}
</section>

<%block name="more_body">
<section>
## facebook
<span>
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/th_TH/all.js#xfbml=1&appId=${request.registry.settings.get('velruse.facebook.consumer_key')}";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<div class="fb-like" data-href="${request.current_route_url()}" data-width="100" data-height="50" data-colorscheme="light" data-layout="button_count" data-action="like" data-show-faces="true" data-send="false"></div>
</span>
## twitter
<span>
    <a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-via="pumbaa">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
</span>
## google plus
<span>
	<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script>
	<g:plusone></g:plusone>
</span>
</section>
% if topic.comments_disabled == False:
<section title="do-comments">
	<form action="${request.route_path('forums.comments.comment', topic_id=topic.id)}" method="post">
		<div class="form-group">
		    <label for="comment">Comment</label>
		    <textarea name="message" rows="5" class="form-control" placeholder="Put your comment"></textarea>
		</div>
		<button type="submit">Submit</button>
	</form>
</section>
% endif
<section title="comments" style="margin-top: 10px;">
% for comment in topic.comments:
	<div class="well">
		<p>${comment.message}</p>
		<p><b>${comment.author.username}</b> | ${comment.published_date}</p>
	</div>
% endfor
</section>
</%block>