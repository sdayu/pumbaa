from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pumbaa import models

@view_config(route_name='manager.topics.index', 
             permission='member',
             renderer='/manager/topics/index.mako')
def index(request):
    topics = models.Topic.objects(status__ne='delete', author=request.user).all()
    return dict(
                topics=topics
                )
    
@view_config(route_name='manager.topics.problem', 
             permission='topic',
             renderer='/manager/topics/problem.mako')
def problem(request):
    topics = models.Topic.objects(status__nin=['delete', 'publish']).all()
    return dict(
                topics=topics
                )

@view_config(route_name='manager.topics.change_status', 
             permission='topic', )
def change_status(request):
    topic_id = request.matchdict.get('topic_id')
    status = request.matchdict.get('status')
    
    default_status = ['publish', 'suspend', 'delete']
    if status not in default_status:
        return Response('This status not allow', status='500')
    
    topic = models.Topic.objects.with_id(topic_id)
    if topic is None:
        return Response('Not Found, topic title:%s'%topic_id, status='404 Not Found')
    
    topic.status = status
    topic.save()
    
    if status == 'delete':
        return HTTPFound(location=request.route_path('manager.topics.problem'))
    
    return HTTPFound(location=request.route_path('forums.topics.index'))