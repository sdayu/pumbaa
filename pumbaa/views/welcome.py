from pyramid.view import view_config
from pumbaa import models

import datetime

import mongoengine as me


@view_config(route_name='index', renderer='/welcome/index.mako')
def index(request):
    recent_topics = models.Topic.objects(status='publish', type='topic').order_by('-published_date').limit(10).all()
    last_comments_topics_ = models.Topic.objects(status='publish', type='topic').order_by('-comments__published_date').limit(10).all()
    last_comments_topics = []
    for topic in last_comments_topics_:
        if len(topic.comments) > 0:
            last_comments_topics.append(topic)
    
    photo_albums_ = models.PhotoAlbum.objects(status='publish').order_by('-published_date').limit(10).all()
    photo_albums = []
    for photo_album in photo_albums_:
        if len(photo_album.photos)> 0:
            photo_albums.append(photo_album)
            
    events = models.Event.objects((me.Q(status='publish') &
                                  (me.Q(started_date__gt=datetime.datetime.now().date()) | 
                                  me.Q(ended_date__gt=datetime.datetime.now())) &
                                  me.Q(event_type__in=['undergraduate', 'graduate', 'department', 'university'])))\
                        .order_by('+started_date')\
                        .limit(5).all()
    
    return dict(
                recent_topics=recent_topics,
                last_comments_topics=last_comments_topics,
                photo_albums=photo_albums,
                events=events
                )
