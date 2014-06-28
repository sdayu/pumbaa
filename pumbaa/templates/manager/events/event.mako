<%inherit file="/manager/base/base.mako"/>

<%block name="addition_header">
	## mark down
	<link rel="stylesheet" type="text/css" href="/public/css/pagedown.css" />
        
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Converter.js"></script>
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Sanitizer.js"></script>
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Editor.js"></script>
	<script type="text/javascript" src="/public/bower_components/pagedown/Markdown.Extra.js"></script>

	## pretty print
	<script type="text/javascript" src="/public/bower_components/google-code-prettify/src/prettify.js"></script> 
	<link rel="stylesheet" type="text/css" href="/public/bower_components/google-code-prettify/src/prettify.css" />

	## select2
	<link rel="stylesheet" type="text/css" href="/public/bower_components/select2/select2.css" />
	<link rel="stylesheet" type="text/css" href="/public/bower_components/select2/select2-bootstrap.css" />
	<script type="text/javascript" src="/public/bower_components/select2/select2.js"></script>
	
	## bootstrap-datetimepicker
	<script type="text/javascript" src="/public/bower_components/moment/min/moment.min.js"></script>
	<link rel="stylesheet" type="text/css" href="/public/bower_components/bootstrap3-datetimepicker/build/css/bootstrap-datetimepicker.min.css" />
	<script type="text/javascript" src="/public/bower_components/bootstrap3-datetimepicker/build/js/bootstrap-datetimepicker.min.js"></script>
	
	<script type="text/javascript">
	function check_event_type(){
		var type = $('#event_type').val();

		if (type == 'conference') {
			$('#conference').show();
		}
		else{
			$('#conference').hide();
		}
	}
	
	$(document).ready(function(){
		
		## markdown script
		(function () {

		    ## var converter = Markdown.getSanitizingConverter();
		    var converter = new Markdown.Converter();
		    
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

		    var editor = new Markdown.Editor(converter);
		    editor.hooks.chain("onPreviewRefresh", prettyPrint); // google code prettify
		    editor.hooks.chain("onPreviewRefresh", function() {
		        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
		    });
		    editor.run();
		})();

		## google-code-prettify
		document.addEventListener('DOMContentLoaded',function() {
		    prettyPrint();
		});

		## select2
		$("#tags").select2({
		    tags:${tags | n},
		    placeholder: "Enter tags: pumbaa, CoE, tag",
		    tokenSeparators: [","],
		    maximumInputLength: 30
		});
		
		$(function () {
            $('#started_date_picker').datetimepicker();
            $('#updated_date_picker').datetimepicker();
            $('#paper_deadline_date_picker').datetimepicker();
            $('#notification_date_picker').datetimepicker();
        });
		
		
		check_event_type();
	});
	
	
	</script>
</%block>

<%block name="title">Events</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.events.index')}">Events</a></li>
	<li><a href="${request.current_route_path()}">Create Event</a></li>
</%block>
<%block name="panel_title">Create Calendars</%block>
<form action="${request.current_route_path()}" method="post" accept-charset="utf-8">
	<div class="form-group${' has-error' if form.title.errors else ''}">
	    <label class="control-label">Title</label>
		% if form.title.errors:
			<span class="text-danger">${form.title.errors[0]}</span>
		% endif
		${form.title(class_='form-control')}
	</div>	
	<div class="row">
		<div class="col-md-6 col-lg-6">
			<div id="wmd-button-bar"></div>
			<div class="form-group${' has-error' if form.description.errors else ''}">
		    <label class="control-label">Description</label>
			% if form.description.errors:
				<span class="text-danger">${form.description.errors[0]}</span>
			% endif
			${form.description(class_='form-control', placeholder='Enter description', rows='10', id="wmd-input")}
		</div>
		</div>
		<div class="col-md-6 col-lg-6">
			<b>Preview</b>
			<div id="wmd-preview" class="well well-sm"></div>
		</div>
	</div>
	<div class="row">
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.started_date.errors else ''}">
				<label class="control-label">From</label>
				% if form.started_date.errors:
					<span class="text-danger">${form.started_date.errors[0]}</span>
				% endif
				<div class='input-group date' id='started_date_picker' data-date-format="DD/MM/YYYY HH:mm">
					${form.started_date(class_='form-control')}
					<span class="input-group-addon">
						<span class="glyphicon glyphicon-time"></span>
					</span>
				</div>
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.ended_date.errors else ''}">
				<label class="control-label">To</label>
				% if form.ended_date.errors:
					<span class="text-danger">${form.ended_date.errors[0]}</span>
				% endif
				<div class='input-group date' id='updated_date_picker' data-date-format="DD/MM/YYYY HH:mm">
					${form.ended_date(class_='form-control')}
					<span class="input-group-addon">
						<span class="glyphicon glyphicon-time"></span>
					</span>
				</div>
			</div>
		</div>
	</div>
	
	<label class="checkbox-inline">
		${form.all_day} All day
	</label>
	<label class="checkbox-inline">
		## ${form.repeat} Repeat
	</label>
	<div class="form-group${' has-error' if form.event_type.errors else ''}">
	    <label class="control-label">Event Type</label>
		% if form.event_type.errors:
			<span class="text-danger">${form.event_type.errors[0]}</span>
		% endif
		${form.event_type(class_='form-control', onclick='check_event_type()')}
	</div>
	
	<div class="row" id="conference">
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.conference.paper_deadline_date.errors else ''}">
				<label class="control-label">Paper deadline</label>
				% if form.conference.paper_deadline_date.errors:
					<span class="text-danger">${form.conference.paper_deadline_date.errors[0]}</span>
				% endif
				<div class='input-group date' id='paper_deadline_date_picker' data-date-format="DD/MM/YYYY">
					${form.conference.paper_deadline_date(class_='form-control')}
					<span class="input-group-addon">
						<span class="glyphicon glyphicon-time"></span>
					</span>
				</div>
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group${' has-error' if form.conference.notification_date.errors else ''}">
				<label class="control-label">Notification Date</label>
				% if form.conference.notification_date.errors:
					<span class="text-danger">${form.conference.notification_date.errors[0]}</span>
				% endif
				<div class='input-group date' id='notification_date_picker' data-date-format="DD/MM/YYYY">
					${form.conference.notification_date(class_='form-control')}
					<span class="input-group-addon">
						<span class="glyphicon glyphicon-time"></span>
					</span>
				</div>
			</div>
		</div>
	</div>


	<div class="form-group${' has-error' if form.venue.errors else ''}">
	    <label class="control-label">Where</label>
		% if form.venue.errors:
			<span class="text-danger">${form.venue.errors[0]}</span>
		% endif
		${form.venue(class_='form-control')}
	</div>
	<div class="form-group${' has-error' if form.tags.errors else ''}">
	    <label class="control-label">Tags</label>
		% if form.tags.errors:
			<span class="text-danger">${form.tags.errors[0]}</span>
		% endif
		<br/>
		${form.tags(class_='form-control', placeholder='Add tags')}
		
	</div>
	<button type="submit" class="btn btn-primary">Add new event</button>
	
</form>
