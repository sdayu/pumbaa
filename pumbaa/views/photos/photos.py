'''
Created on Nov 10, 2013

@author: boatkrap
'''
from pumbaa.views.photos import photo_albums
'''
Created on Jul 14, 2012

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from pumbaa import models
 
@view_config(route_name='photos.view')
def view(request):
    matchdict = request.matchdict
    photo_album_id = matchdict['photo_album_id']
    photo_id = matchdict['photo_id']
     
    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    image = photo_album.get_photo(photo_id).get_image()
    
    response = Response()
    extension = image.filename[image.filename.rfind('.')+1:]

    if extension.lower() in ['jpg', 'jpeg']:
        response.content_type='image/jpeg'
    elif extension.lower() in ['png']:
        response.content_type='image/png'
 
    response.body_file = image
    return response
 
 
@view_config(route_name='photos.thumbnail')
def thumbnail(request):
    matchdict = request.matchdict

    photo_album_id = matchdict['photo_album_id']
    photo_id = matchdict['photo_id']

    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    image = photo_album.get_photo(photo_id).image
    
    extension = image.filename[image.filename.rfind('.')+1:]
    
    if image.thumbnail:
        image = image.thumbnail
        
    response = Response()

    if extension.lower() in ['jpg', 'jpeg']:
        response.content_type='image/jpeg'
    elif extension.lower() in ['png']:
        response.content_type='image/png'
 
    response.body_file = image
    return response