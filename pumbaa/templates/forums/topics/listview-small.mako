<%page args="topics" />

<%! 
    from datetime import datetime, timedelta 
    def tooltip_getDays(uptime, diffTime):

        if diffTime.days < 0:
            return "???"
        if diffTime.days < 1:
            return tooltip_getTimes(diffTime.seconds)
        elif diffTime.days < (1*2):
            return "%d day" % (diffTime.days)
        elif diffTime.days < 7:
            return "%d days" % (diffTime.days)
        elif diffTime.days < (7*2):
            return "%d week" % (diffTime.days/7)
        else:
            return uptime.strftime("%b %d, %Y")

    def tooltip_getTimes(times):
        if times < (1*2):
            return "1 sec"
        elif times < 60:
            return "%d secs" % (times)
        elif times < (60*2):
            return "%d min" % (times/60)
        elif times < (60*60):
            return "%d mins" % (times/60)
        elif times < (60*60*2):
            return "%d hr" % (times/3600)
        else:
            return "%d hrs" % (times/3600)
%>

<ul class="list-group">
% for topic in topics:

<%
    topic_timenow  = datetime.now()
    topic_timediff = topic_timenow - topic.updated_date

    topic_author_tooltip = "By %s (%s)" % (
        topic.author.get_display_name(),
        tooltip_getDays(topic.updated_date, topic_timediff)
    )
%>
    <li class="list-group-item">
            <span data-toggle="tooltip" data-placement="top" title="${topic_author_tooltip}">
                <a href="${request.route_path('forums.topics.view', 
                    title=topic.title, topic_id=topic.id)}">${topic.title}</a>
            </span>
            <div class="pull-right">
                % if len(topic.comments) > 0:
<%
    last_comment_timediff = topic_timenow - topic.comments[len(topic.comments)-1].updated_date
%>
                    <small class="ptopic-small">
                        ${topic.comments[len(topic.comments)-1]\
                           .author.get_tim_display_name()}
                        % if last_comment_timediff.days >= 0 and last_comment_timediff.days <= 1:
                            <span class="badge badge-update">${len(topic.comments)} </span>
                        % else:
                            <span class="badge">${len(topic.comments)} </span>
                        % endif
                    </small>
                % endif

                % if topic_timediff.days >= 0 and topic_timediff.days <= 1:
                    <span class="label label-warning">Today</span>
                % endif
            </div>
    </li>
%endfor
</ul>

<script type="text/javascript">
$(document).ready(function() {
    // Tooltip
    $('[data-toggle="tooltip"]').tooltip();
    //    "title"="Created by ${topic.author.get_display_name()}"
    // });
});
</script> 

