<%inherit file="/forums/base/base.mako"/>
<%! import markdown %>
<%block name="addition_header">
	<link rel="stylesheet" type="text/css" href="/public/libs/markdown/pagedown/demo.css" />
        
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Converter.js"></script>
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Sanitizer.js"></script>
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Editor.js"></script>
</%block>
<%block name="title">${topic.title}</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
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

<article title="topic description">
${markdown.markdown(topic.description, extensions=['codehilite(linenums=True)']) | n}
</article>

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

<section title="do-comments">
	<form action="${request.route_path('forums.comments.comment', topic_id=topic.id)}" method="post">
	<div class="row">
		<div class="col-md-6 col-lg-6">
			<div id="wmd-button-bar"></div>
			<div class="form-group">
			    <label for="comment">Comment</label>
			    <textarea id="wmd-input" name="message" rows="5" class="form-control" placeholder="Put your comment"></textarea>
			</div>
		</div>
		<div class="col-md-6 col-lg-6">
			<b>Preview</b>
			<div id="wmd-preview" class="well well-sm"></div>
		</div>
	</div>
		<button type="submit">Submit</button>
	</form>
</section>

## markdown script
<script type="text/javascript">
    (function () {
        var converter1 = Markdown.getSanitizingConverter();
        
        converter1.hooks.chain("preBlockGamut", function (text, rbg) {
            return text.replace(/^ {0,3}""" *\n((?:.*?\n)+?) {0,3}""" *$/gm, function (whole, inner) {
                return "<blockquote>" + rbg(inner) + "</blockquote>\n";
            });
        });
        
        var editor1 = new Markdown.Editor(converter1);
        
        editor1.run();
    })();
</script>

<section title="comments" style="margin-top: 10px;">
% for comment in topic.comments:
	<div class="well well-sm">
		<section title="comment">
		${markdown.markdown(comment.message, extensions=['codehilite(linenums=True)']) | n}
		<p>${'' if comment.author.get_profile_picture() is None else comment.author.get_profile_picture() | n}
		<b>${comment.author.username}</b> | ${comment.published_date}</p>
		</section>
	</div>
% endfor
</section>
</%block>