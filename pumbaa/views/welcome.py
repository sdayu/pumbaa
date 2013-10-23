from pyramid.view import view_config
from pumbaa import models

@view_config(route_name='index', renderer='/welcome/index.mako')
def index(request):
    recent_topics = models.Topic.objects(status='publish', page=False).order_by('-published_date').limit(25).all()
    last_comments_topics = models.Topic.objects(status='publish', page=False).order_by('-comments__published_date').limit(15).all()
    forums = models.Forum.objects(status='publish').all()
    return dict(
                recent_topics=recent_topics,
                last_comments_topics=last_comments_topics,
                forums=forums
                )
