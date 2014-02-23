'''
Created on Nov 9, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pumbaa import models, forms

import tempfile
from PIL import Image
from PIL.ExifTags import TAGS
from http.client import HTTPResponse

@view_config(route_name='manager.photo_albums.index', 
             permission='member',
             renderer='/manager/photo_albums/index.mako')
def index(request):
    my_photo_albums = models.PhotoAlbum.objects(status__ne='delete', user=request.user).all()
    share_photo_albums = models.PhotoAlbum.objects(status__ne='delete', shared="True", user__ne=request.user).all()
    
    return dict(
                my_photo_albums=my_photo_albums,
                share_photo_albums=share_photo_albums
                )

@view_config(route_name='manager.photo_albums.create', 
             permission='member',
             renderer='/manager/photo_albums/create.mako')
@view_config(route_name='manager.photo_albums.edit', 
             permission='member',
             renderer='/manager/photo_albums/create.mako')
def create_edit(request):
    form = forms.photos.PhotoAlbum(request.POST)
    if len(request.POST) == 0 or not form.validate():
        return dict(
                    form=form
                    )
    photo_albums = models.PhotoAlbum(**form.data)
    photo_albums.status = 'publish'
    photo_albums.user = request.user

    photo_albums.save()
    
    return HTTPFound(location=request.route_path('manager.photo_albums.index'))

@view_config(route_name='manager.photo_albums.add_photo', 
             permission='member',
             renderer='/manager/photo_albums/add_photo.mako')
def add_photo(request):
    
    form = forms.photos.Photo(request.POST)
    form.license.choices = [(license, license) for license in models.photos.LICENSE]
    
    if len(request.POST) == 0 or not form.validate():
        form.license.data = 'COPYRIGHT'
        return dict(
                    form=form
                    )
        
    photo_album  = models.PhotoAlbum.objects.with_id(request.matchdict.get('photo_album_id'))
    
    images = request.POST.getall('image')
    license = form.data.get('license')
    
    if images is not None and type(images) == list:
        if len(images) > 0:
            if type(images[0]) == bytes:
                return HTTPFound(location=request.current_route_path())
        for image in images:
            photo = models.Photo()
            
            img = Image.open(image.file)

            image.file.seek(0)
            img_format = img.format
            
            orientation = 0
            if img._getexif() is not None:
                for k, v in img._getexif().items():
                    if TAGS.get(k, k) == 'Orientation':
                        orientation = v
                        break
            
            if orientation == 8:
                photo.orientation = 'vertical'
            if orientation == 6:
                photo.orientation = 'vertical'
                img = img.transpose(Image.ROTATE_180)

            
            if img.size[0] < img.size[1]:
                photo.orientation = 'vertical'
                img = img.transpose(Image.ROTATE_270)
            
            
            tmp_img = tempfile.TemporaryFile()
             
            img.save(tmp_img, format=img_format)
            tmp_img.seek(0)

            photo.image.put(tmp_img, filename=image.filename, exif=img.info['exif'])
                
            photo.license = license
            photo.user = request.user
            photo_album.photos.append(photo)
            photo_album.save()
    return HTTPFound(location=request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id))

@view_config(route_name='manager.photo_albums.delete', 
             permission='member')
def delete(request):
    photo_album_id = request.matchdict.get('photo_album_id')
    photo_album = models.PhotoAlbum.objects(id=photo_album_id, user=request.user).first()
    
    if photo_album is None:
        return HTTPResponse("Permission Denied")
    
    photo_album.status = "delete"
    photo_album.save()
    
    return HTTPFound(location=request.route_path('manager.photo_albums.index'))
