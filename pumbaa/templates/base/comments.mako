<%page args="item"/>
<%!
	import json
	from pumbaa import models
%>
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

    ## converter = Markdown.getSanitizingConverter();
    converter = new Markdown.Converter();
    
    converter.hooks.chain("preBlockGamut", function (text, rbg) {
        return text.replace(/^ {0,3}""" *\n((?:.*?\n)+?) {0,3}""" *$/gm, function (whole, inner) {
            return "<blockquote>" + rbg(inner) + "</blockquote>\n";
        });
    });

    converter.hooks.chain("postConversion", function(text) {
        return text.replace(/\s*:::(:)*python\s*\n/, "");
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

## angularjs
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.8/angular.min.js"></script>
## end angularjs

</%block>

<%
    comments = item.comments
    self.editor_counter = 0
%>

<%block name="do_comment" args="item">

<%
    	
    self.editor_counter += 1
    comment_url = None
    if type(item) == models.Topic:
    	comment_url = request.route_path('forums.comments.comment', topic_id=item.id)
    elif type(item) == models.Comment:
    	comment_url = request.route_path('forums.comments.reply', topic_id=item.get_topic().id, comment_id=item.id)
    elif type(item) == models.PhotoAlbum:
        comment_url = request.route_path('photos.photo_albums.comment', photo_album_id=item.id)
    elif type(item) == models.Photo:
        comment_url = request.route_path('photos.photo_albums.photo_comment', photo_album_id=item.get_album().id, photo_id=item.id)

    comments_disabled = False
    if hasattr(item, 'comments_disabled'):
        comments_disabled = item.comments_disabled
%>

## for disable comments
% if not comments_disabled:

<section title="Share your opinion" class="well">
% if request.user:
    % if request.user.get_role('anonymous'):
        คุณยังไม่มีสิทธิ์ใช้งานส่วนแสดงความคิดเห็น กรุณาติดต่อสมาชิกที่รู้จักเพื่อยืนยันว่าคุณเป็นส่วนหนึ่งของ CoE
    % else:
    <form action="${comment_url}" method="post">
        <div class="row">
            <div class="col-md-1 col-lg-1">
            <section title="who comment">
                <p>
                    ${'' if request.user.get_profile_picture() is None else request.user.get_profile_picture() | n}
                    <b>${request.user.username}</b>
                </p>
            </section>
            </div>
            <div class="col-md-6 col-lg-6">
                <div id="wmd-button-bar-${self.editor_counter}"></div>
                <div class="form-group">
                    <label for="comment">Comment</label>
                    <textarea id="wmd-input-${self.editor_counter}" name="message" rows="5" class="form-control" placeholder="Share your comment"></textarea>
                </div>
            </div>
            <div class="col-md-5 col-lg-5">
                <b>Preview</b>
                <div id="wmd-preview-${self.editor_counter}" class="well well-sm"></div>
            </div>
        </div>
        <button type="submit">Share comment</button> 
        แนะนำวิธีการเขียน <a href="${request.route_path('pages.view', title='writing guideline')}">Markdown</a>
    </form>
    % endif
% else:
    <a href="${request.route_path('login')}">Log in</a> ก่อนแสดงความคิดเห็น
% endif
</section>

% endif
## end disable comments
</%block>

<section title="comments" style="margin-top: 10px;" ng-app>
<h4><b>ความคิดเห็น</b></h4>

<% render_comment_id = [] %>
<%def name="show_comment(comment, order='1')">
<%
    if comment.status == 'publish':
        render_comment_id.append({'id':"#%s"%comment.id, 'message':comment.message})
    else:
        render_comment_id.append({'id':"#%s"%comment.id, 'message':'ความเห็นนี้รอการพิจารณา'})
%>
	<section title="comment">
        <div class="panel panel-info">
           <div class="panel-heading">
              ความคิดเห็นที่ ${order}
          </div>
          <div class="panel-body">
          	<div class="row">
          		<div class="col-sm-2 col-md-2 col-lg-2">
          			<p>${'' if comment.author.get_profile_picture() is None else comment.author.get_profile_picture() | n}</p>
            		<p><b>${comment.author.username}</b></p>
            		<p>
            			${comment.published_date.ctime()}
            		</p>
          		</div>
          		<div class="col-sm-10 col-md-10 col-lg-10">
                <div id="${comment.id}">
                % if comment.status == 'publish':
                    ${comment.message}
                % endif
                </div>
                <p class="text-right">
                % if order.count('-') < 2 and (not (type(item) == models.PhotoAlbum or type(item) == models.Photo)):
            		<a href="" ng-click="reply_${comment.id} = !reply_${comment.id}">ตอบกลับ</a>
            	% endif
                </p>
                </div>
            </div>
          </div>
          <div class="panel-footer">
            % if order.count('-') < 2 and (not (type(item) == models.PhotoAlbum or type(item) == models.Photo)):
       	 		<div ng-show="reply_${comment.id}">
        		${self.do_comment(comment)}
        		</div>
				<div ng-hide="reply_${comment.id}"></div>
			% endif
			% for i in range(0, len(comment.replies)):
    		<%
    			reply = comment.replies[i] 
    			reply.topic = topic    		
    		%>
    		${show_comment(reply, order+"-"+str(i+1))}
    		
			% endfor
          </div>
        </div>
        
    </section>
</%def>

% for i in range(0, len(comments)):
    <% comment = comments[i] %>
    ${show_comment(comment, str(i+1))}
% endfor

<script type="text/javascript">
var comments = ${json.dumps(render_comment_id) | n};
$( document ).ready(function() {
    comments.forEach(function(entry) {
        $(entry.id).html(converter.makeHtml(entry.message));
    });
});
</script>

</section>

## markdown editor
<script type="text/javascript">
(function () {
	% for i in range(1, self.editor_counter+1):
    var editor${i} = new Markdown.Editor(converter,"-${i}");
    editor${i}.hooks.chain("onPreviewRefresh", prettyPrint); // google code prettify
    editor${i}.hooks.chain("onPreviewRefresh", function() {
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    });
    editor${i}.run();
    % endfor
})();
</script>