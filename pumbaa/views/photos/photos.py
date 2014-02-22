'''
Created on Jul 14, 2012

@author: boatkrap
'''

from pumbaa.views.photos import photo_albums

from PIL import Image
import tempfile

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
    photo = photo_album.get_photo(photo_id)
    
    response = Response()
    extension = photo.image.filename[photo.image.filename.rfind('.')+1:]

    if extension.lower() in ['jpg', 'jpeg']:
        response.content_type='image/jpeg'
    elif extension.lower() in ['png']:
        response.content_type='image/png'
 
    img = Image.open(photo.image)
    img_format = img.format
    if photo.orientation == 'vertical':
        img = img.transpose(Image.ROTATE_90)
 
    tmp_img = tempfile.TemporaryFile()
             
    img.save(tmp_img, format=img_format)
    tmp_img.seek(0)
    
    response.body_file = tmp_img
    return response
 
 
@view_config(route_name='photos.thumbnail')
def thumbnail(request):
    matchdict = request.matchdict

    photo_album_id = matchdict['photo_album_id']
    photo_id = matchdict['photo_id']

    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    photo = photo_album.get_photo(photo_id)
    
    extension = photo.image.filename[photo.image.filename.rfind('.')+1:]
    
    if photo.image.thumbnail:
        image = photo.image.thumbnail
        
    response = Response()

    if extension.lower() in ['jpg', 'jpeg']:
        response.content_type='image/jpeg'
    elif extension.lower() in ['png']:
        response.content_type='image/png'
 
    
    img = Image.open(image)
    img_format = img.format

    if photo.orientation == 'vertical':
        img = img.transpose(Image.ROTATE_90)
 
    tmp_img = tempfile.TemporaryFile()
             
    img.save(tmp_img, format=img_format)
    tmp_img.seek(0)
 
    response.body_file = tmp_img
    return response