<%page args="topics" />
    
<ul class="list-unstyled">
% for topic in topics:
    <li>
        <div>
            <a href="${request.route_path('forums.topics.view', 
                    title=topic.title, topic_id=topic.id)}">
            <h4>${topic.title}</h4>
            </a>
            <div class="ptopic-xs">
                <span class="glyphicon glyphicon-user"></span>
                <a href="#">${topic.author.get_tim_display_name()}</a>
                <div class="pull-right">
                    % if len(topic.comments) > 0:
                        ${topic.comments[len(topic.comments)-1]\
                            .author.get_tim_display_name()}
                        <span class="badge">${len(topic.comments)} </span>
                    % endif
                 </div>
            </div>
        </div>
    </li>
%endfor
</ul>
