'''
Created on Nov 10, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pumbaa import models

@view_config(route_name='photos.photo_albums.index',
             renderer='/photos/photo_albums/index.mako')
def index(request):
    photo_albums = models.PhotoAlbum.objects(status="publish").all()
    return dict(
                photo_albums=photo_albums
                )

@view_config(route_name='photos.photo_albums.view',
             renderer='/photos/photo_albums/view.mako')
def view(request):
    photo_album = models.PhotoAlbum.objects.with_id(request.matchdict.get('photo_album_id'))
    return dict(
                photo_album=photo_album
                )