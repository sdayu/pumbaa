from pyramid.view import view_config
from pumbaa import models

@view_config(route_name='index', renderer='/welcome/index.mako')
def index(request):
    topics = models.Topic.objects.order_by('published_date').limit(10).all()
    return dict(
                topics=topics
                )
