'''
Created on Oct 18, 2013

@author: boatkrap
'''

from pumbaa import models
import math

# @view_config(route_name='forums.index', 
#              renderer='/forums/forums/index.mako')
def index(request):
    forums = models.Forum.objects(status='publish').all()
    return dict(
                forums=forums
                )
    
# @view_config(route_name='forums.view', 
#              renderer='/forums/forums/view.mako')
def view(request):
    name = request.matchdict.get('name')
    forum = models.Forum.objects(name=name, status='publish').first()
    if forum is None:
        return Response('Forum name: %s not found!'%name, status='404 Not Found')
    
    
    page = int(request.GET.get('page', 1))
    topics_per_page = 15
    
    topic_count = models.Topic.objects(tags__in=forum.tags, status='publish').count()
    pages = math.ceil(topic_count/topics_per_page)
    
    page = page if page > 0 else 1
    page = page if page <= pages else pages
    
    topics = models.Topic.objects(tags__in=forum.tags, status='publish').order_by('-published_date').skip((page-1)*topics_per_page).limit(topics_per_page).all()
    
    
    return dict(
                forum=forum,
                topics=topics,
                page=page,
                pages=pages
                )
