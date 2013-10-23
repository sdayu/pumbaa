<%inherit file="/forums/base/base.mako"/>
<%! import json %>
<%block name="addition_header">
	<link rel="stylesheet" type="text/css" href="/public/libs/markdown/pagedown/demo.css" />
        
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Converter.js"></script>
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Sanitizer.js"></script>
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Editor.js"></script>
	<script type="text/javascript" src="/public/libs/markdown/pagedown/Markdown.Extra.js"></script>
	
	<script type="text/javascript" src="/public/libs/google-code-prettify/prettify.js"></script> 
	<link rel="stylesheet" type="text/css" href="/public/libs/google-code-prettify/prettify.css" />

## markdown script
<script type="text/javascript">
var converter;
(function () {

	converter = Markdown.getSanitizingConverter();
    
    converter.hooks.chain("preBlockGamut", function (text, rbg) {
        return text.replace(/^ {0,3}""" *\n((?:.*?\n)+?) {0,3}""" *$/gm, function (whole, inner) {
            return "<blockquote>" + rbg(inner) + "</blockquote>\n";
        });
    });
    
    Markdown.Extra.init(converter, {
      extensions: "all",
      highlighter: "prettify"
    });
    
})();
</script>

## google-code-prettify
<script type='text/javascript'>
document.addEventListener('DOMContentLoaded',function() {
    prettyPrint();
});
</script>

</%block>
<%block name="title">${topic.title}</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
</%block>
<%block name="panel_title">${topic.title}</%block>
   
<%block name="panel_footer">
	  <div class="panel-footer">

		<p>${'' if topic.author.get_profile_picture() is None else topic.author.get_profile_picture() | n}
		<b>${topic.author.username}</b> | ${topic.published_date}</p>

	  </div>
</%block>

<section>
	<article title="topic description" id="description">
	${topic.description}
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
    $("#description").html(converter.makeHtml(${json.dumps(topic.description) | n}));
});
</script>

<%block name="more_body">

<%include file="/base/social_integration.mako"/>

% if topic.comments_disabled == False:
<section title="do-comments">
	<form action="${request.route_path('forums.comments.comment', topic_id=topic.id)}" method="post">
	<div class="row">
		<div class="col-md-6 col-lg-6">
			<div id="wmd-button-bar"></div>
			<div class="form-group">
			    <label for="comment">Comment</label>
			    <textarea id="wmd-input" name="message" rows="5" class="form-control" placeholder="Share your comment"></textarea>
			</div>
		</div>
		<div class="col-md-6 col-lg-6">
			<b>Preview</b>
			<div id="wmd-preview" class="well well-sm"></div>
		</div>
	</div>
		<button type="submit">Share comment</button>
	</form>
</section>
% endif

## markdown editor
<script type="text/javascript">
(function () {
    var editor1 = new Markdown.Editor(converter);
    editor1.hooks.chain("onPreviewRefresh", prettyPrint); // google code prettify
    editor1.run();
})();
</script>

<section title="comments" style="margin-top: 10px;">
<script type="text/javascript">
var comments = ${json.dumps([{'id':"#%s"%comment.id, 'message':comment.message} for comment in topic.comments]) | n};
$( document ).ready(function() {
	comments.forEach(function(entry) {
    	$(entry.id).html(converter.makeHtml(entry.message));
	});
});
</script>

% for comment in topic.comments:
	<section title="comment">
		<div class="panel panel-info">
		  <div class="panel-body">
			    <div id="${comment.id}">
					${comment.message}
				</div>
		  </div>
		  <div class="panel-footer">
		  	<p>${'' if comment.author.get_profile_picture() is None else comment.author.get_profile_picture() | n}
			<b>${comment.author.username}</b> | ${comment.published_date}</p>
		  </div>
		</div>
	</section>
% endfor
	
</section>
</%block>
