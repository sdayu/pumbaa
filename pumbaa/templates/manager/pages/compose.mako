<%inherit file="/manager/base/base.mako"/>
<%block name="addition_header">
	<link rel="stylesheet" type="text/css" href="/public/css/pagedown.css" />
        
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Converter.js"></script>
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Sanitizer.js"></script>
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Editor.js"></script>
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Extra.js"></script>
	
	<script type="text/javascript" src="/public/bower_components/google-code-prettify/src/prettify.js"></script> 
	<link rel="stylesheet" type="text/css" href="/public/bower_components/google-code-prettify/src/prettify.css" />
	
	<link rel="stylesheet" type="text/css" href="/public/bower_components/select2/select2.css" />
	<script type="text/javascript" src="/public/bower_components/select2/select2.js"></script>
</%block>
<%block name="title">New Pages</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.pages.index')}">Pages</a></li>
	<li class="active">New page</li>
</%block>

<%block name="panel_title">New Page</%block>
<form action="${request.current_route_path()}" method="post">
	<div class="form-group${' has-error' if form.title.errors else ''}">
	    <label for="title" class="control-label${' has-error' if form.title.errors else ''}">Title</label>
	    % if form.title.errors:
			<span class="text-danger">${form.title.errors[0]}</span>
		% endif
	    ${form.title(class_='form-control', placeholder='Enter title')}
	</div>
	<div class="row">
		<div class="col-md-6 col-lg-6">
			<div id="wmd-button-bar"></div>
			<div class="form-group${' has-error' if form.description.errors else ''}">
			    <label for="description" class="control-label${' has-error' if form.description.errors else ''}">Description</label>
			    ${form.description(class_='form-control', placeholder='Enter description', rows='10', id="wmd-input")}
			    <p style="margin-top: 10px;">
			     เขียน description ด้วย <a target="_blank" href="http://en.wikipedia.org/wiki/Markdown">MarkDown</a>
			    </p>
			</div>
		</div>
		<div class="col-md-6 col-lg-6">
			<b>Preview</b>
			<div id="wmd-preview" class="well well-sm"></div>
		</div>
	</div>
	<div class="form-group${' has-error' if form.tags.errors else ''}">
	    <label for="tags" class="control-label${' has-error' if form.tags.errors else ''}">Tags</label>
		${form.tags(style="width:100%")}
	</div>
	<div class="form-group${' has-error' if form.comments_disable.errors else ''}">
	<label class="control-label${' has-error' if form.tags.errors else ''}">Comment:</label>
	 % if form.comments_disable.errors:
		<span class="text-danger">${form.comments_disable.errors[0]}</span>
	% endif
	<br/>
	% for subfield in form.comments_disable:
	<div class="radio-inline">
		${subfield}
		${subfield.label}
	</div>
	% endfor
	</div>
	<div class="form-group">
		<button type="submit" class="btn btn-primary">Create page</button>
	</div>
</form>

## markdown script
<script type="text/javascript">
(function () {

    ## var converter = Markdown.getSanitizingConverter();
    var converter = new Markdown.Converter();
    
    converter.hooks.chain("preBlockGamut", function (text, rbg) {
        return text.replace(/^ {0,3}""" *\n((?:.*?\n)+?) {0,3}""" *$/gm, function (whole, inner) {
            return "<blockquote>" + rbg(inner) + "</blockquote>\n";
        });
    });
    
    Markdown.Extra.init(converter, {
      extensions: "all",
      highlighter: "prettify"
    });

    var editor1 = new Markdown.Editor(converter);
    editor1.hooks.chain("onPreviewRefresh", prettyPrint); // google code prettify
    editor1.run();
})();
</script>


## select2
<script type="text/javascript">
$("#tags").select2({
    tags:${tags | n},
    placeholder: "Enter tags: pumbaa, CoE, tag",
    tokenSeparators: [","],
    maximumInputLength: 30
});
</script>

## google-code-prettify
<script type='text/javascript'>
document.addEventListener('DOMContentLoaded',function() {
    prettyPrint();
});
</script>
