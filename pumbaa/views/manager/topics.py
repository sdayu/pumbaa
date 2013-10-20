from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models

@view_config(route_name='manager.topics.index', 
             permission='member', 
             renderer='/manager/topics/index.mako')
def index(request):
    topics = models.Topic.objects(status__ne='delete', author=request.user).all()
    return dict(
                topics=topics
                )