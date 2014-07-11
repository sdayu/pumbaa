'''
Created on Nov 10, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from beaker.cache import cache_region

from pumbaa import models, forms


@cache_region('default_term')
def get_all_albums():
    photo_albums = models.PhotoAlbum.objects(status="publish").order_by('-event_date').all()
    return dict(
            photo_albums=photo_albums
            )


@view_config(route_name='photos.photo_albums.index',
             renderer='/photos/photo_albums/index.mako')
def index(request):
    return get_all_albums()
    


@view_config(route_name='photos.photo_albums.view',
             renderer='/photos/photo_albums/view.mako')
def view(request):
    photo_album = models.PhotoAlbum.objects.with_id(request.matchdict.get('photo_album_id'))
    return dict(
                photo_album=photo_album
                )
    
@view_config(route_name='photos.photo_albums.photo_view',
             renderer='/photos/photo_albums/photo_view.mako')
def photo_view(request):
    
    photo_album = models.PhotoAlbum.objects.with_id(request.matchdict.get('photo_album_id'))
    photo, pprevious, pnext = photo_album.get_photo_index(request.matchdict.get('photo_id'))
    return dict(
                photo_album=photo_album,
                photo=photo,
                pprevious=pprevious,
                pnext=pnext
                )

@view_config(route_name='photos.photo_albums.comment') 
@view_config(route_name='photos.photo_albums.photo_comment')
def photo_comment(request):
    
    photo_album_id = request.matchdict.get('photo_album_id')
    photo_id = request.matchdict.get('photo_id', None)
    
    photo_album = models.PhotoAlbum.objects.with_id(request.matchdict.get('photo_album_id'))
    item = photo_album
    url = request.route_path('photos.photo_albums.view', photo_album_id=photo_album_id)
    
    if photo_id is not None:
        item = item.get_photo(request.matchdict.get('photo_id'))
        url = request.route_path('photos.photo_albums.photo_view', photo_album_id=photo_album_id, photo_id=photo_id)
        
    form = forms.topics.Comment(request.POST)

    if len(request.POST) > 0 and form.validate():
        message = form.data.get('message')
        
    else:
        return HTTPFound(location=url)
    
    comment = models.Comment(message=message, 
                             author=request.user, 
                             status='publish',
                             ip_address=request.environ.get('REMOTE_ADDR'))

    item.comments.append(comment)
    photo_album.save()
    
    return HTTPFound(location=url) 
