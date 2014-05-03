from pyramid.view import view_config
from pumbaa import models

import datetime

@view_config(route_name='index', renderer='/welcome/index.mako')
def index(request):
    servertime = models.PumbaaTime().getTime()
    # servertime = ptime.getTime()

    recent_topics = models.Topic.objects(status='publish', page=False).order_by('-published_date').limit(10).all()
    last_comments_topics_ = models.Topic.objects(status='publish', page=False).order_by('-comments__published_date').limit(10).all()
    last_comments_topics = []
    for topic in last_comments_topics_:
        if len(topic.comments) > 0:
            last_comments_topics.append(topic)
    
    
    forums = models.Forum.objects(status='publish').all()
    photo_albums_ = models.PhotoAlbum.objects(status='publish').order_by('-published_date').limit(10).all()
    photo_albums = []
    for photo_album in photo_albums_:
        if len(photo_album.photos)> 0:
            photo_albums.append(photo_album)
    
    return dict(
                servertime=servertime,
                recent_topics=recent_topics,
                last_comments_topics=last_comments_topics,
                forums=forums,
                photo_albums=photo_albums
                )
