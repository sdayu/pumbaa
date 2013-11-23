'''
Created on Nov 9, 2013

@author: boatkrap
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pumbaa import models, forms
import cgi

@view_config(route_name='manager.photo_albums.index', 
             permission='member',
             renderer='/manager/photo_albums/index.mako')
def index(request):
    photo_albums = models.PhotoAlbum.objects(status__ne='delete').all()
    return dict(photo_albums=photo_albums)

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
        for image in images:
            photo = models.Photo()
            photo.image.put(image.file, filename = image.filename)
            photo.license = license
            photo_album.photos.append(photo)
        photo_album.save()
    return HTTPFound(location=request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id))

@view_config(route_name='manager.photo_albums.delete', 
             permission='member')
def delete(request):
    return dict()