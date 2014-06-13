<%inherit file="/base/default.mako"/>
<%!
	import json
%>
<%block name="addition_header">
<style type="text/css">
.reset-box-sizing,
.reset-box-sizing * {
  -webkit-box-sizing: content-box;
     -moz-box-sizing: content-box;
          box-sizing: content-box;
}
</style>

## for markdown
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
<div class="row">
	<div class="col-sm-6 col-md-6 col-lg-6">
		<section>
			<div class="btn-group-justified" style="padding-bottom: 10px;">
				<a class="btn btn-primary btn-sm" href="${request.route_path('forums.index')}">All forums</a>
				<a class="btn btn-primary btn-sm" href="${request.route_path('forums.topics.index')}">All topics</a>
				<a class="btn btn-primary btn-sm" href="${request.route_path('forums.tags.index')}">All tags</a>
				<a class="btn btn-primary btn-sm" href="${request.route_path('forums.topics.compose')}">New topics</a>
			</div>
		<div class="panel panel-info">
		  <div class="panel-heading">
		    <h3 class="panel-title">Recent Topics <a href="${request.route_path('forums.feeds')}"><img alt="Atom feed" src="/public/images/feed-icon.svg" width=15px/></a></h3>
		  </div>
		  <div class="panel-body">
			  <ul class="list-unstyled">
			    % for topic in recent_topics:
			    	<li><a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a></li>
			    % endfor
			  </ul>
		  </div>
		</div>
		## topic in forums
		% for forum in forums:
		<div class="panel panel-info">
		  <div class="panel-heading">
		    <h3 class="panel-title"><a href="${request.route_path('forums.view', name=forum.name)}">${forum.name}</a> <a href="${request.route_path('forums.feeds.forums', forum_name=forum.name)}"><img alt="Atom feed" src="/public/images/feed-icon.svg" width=15px/></a></h3>
		  </div>
		  <div class="panel-body">
			  <ul class="list-unstyled">
			    % for topic in forum.get_topics(10):
			    	<li><a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a></li>
			    % endfor
			  </ul>
		  </div>
		</div>
		% endfor
		## topic in forums
		
		## start photo
		<div class="panel panel-info">
		  <div class="panel-heading">
		    <h3 class="panel-title"><a href="${request.route_path('photos.photo_albums.index')}">Photo Albums</a></h3>
		  </div>
		  <div class="panel-body">
		  
		  	<div class="row">
		  	% for photo_album in photo_albums[:8]:
			  <div class="col-sm-6 col-md-3 col-lg-3">
			    <a class="thumbnail" href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">
			        <img src="${request.route_path('photos.thumbnail', photo_album_id=photo_album.id, photo_id=photo_album.photos[0].image.filename)}" alt="${photo_album.name}">
			    </a>
			  </div>
			  % endfor
			</div>

		  </div>
		</div>
		## end photo
		</section>
	</div>
	<div class="col-sm-6 col-md-6 col-lg-6">
		<div class="reset-box-sizing">
			<h4 class="text-info">Search</h4>
			<script>
			  (function() {
			    var cx = '012330424726856876039:gyjrvz5ohbo';
			    var gcse = document.createElement('script');
			    gcse.type = 'text/javascript';
			    gcse.async = true;
			    gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
			        '//www.google.com/cse/cse.js?cx=' + cx;
			    var s = document.getElementsByTagName('script')[0];
			    s.parentNode.insertBefore(gcse, s);
			  })();
			</script>
			<gcse:searchbox-only></gcse:searchbox-only>
		</div>
		<div class="panel panel-info">
		  <div class="panel-heading">
		    <h3 class="panel-title">Agenda</h3>
		  </div>
		  <div class="panel-body" style="padding: 0;">
		  	<div class="list-group">
		  		% for event in events:
  				<a href="${request.route_path('calendars.events.view', event_id=event.id)}" class="list-group-item">
  					<h4 class="list-group-item-heading">${event.topic.title}</h4>
  					<p>
  						<i>${event.started_date} - ${event.ended_date}</i><br/>
  						${event.topic.description[:150]}<br/>
  						% if event.venue:
  						<b>where:</b> ${event.venue}
  						% endif
  					</p>
  				</a>
  				% endfor
		  	</div>
		  </div>
		</div>
		<div class="panel panel-info">
		  <div class="panel-heading">
		    <h3 class="panel-title">Last Comments </h3>
		  </div>
		  <div class="panel-body">
		  	<% comments = [] %>
			% for topic in last_comments_topics:
				<% comments.append(topic.comments[-1]) %>
				<div class="well well-sm">
					<div>
						<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
					</div>
					<div id="${topic.comments[-1].id}">
						${topic.comments[-1].message}
					</div>
					<div>
						<div class="pull-left">
							${'' if topic.comments[-1].author.get_profile_picture() is None else topic.comments[-1].author.get_profile_picture() | n}
						</div>
						<div>
							<b>${topic.comments[-1].author.get_display_name()}</b> <br/>${topic.comments[-1].published_date}
						</div>
					</div>
				</div>
			
			% endfor
		  </div>
		</div>
		
		<script type="text/javascript">
		var comments = ${json.dumps([{'id':"#%s"%comment.id, 'message':comment.message} if comment.status == 'publish' else {'id':"#%s"%comment.id, 'message':'ความเห็นนี้รอการพิจารณา'} for comment in comments]) | n};
		$( document ).ready(function() {
			comments.forEach(function(entry) {
		    	$(entry.id).html(converter.makeHtml(entry.message));
			});
		});
		</script>
		
	</div>
</div>

