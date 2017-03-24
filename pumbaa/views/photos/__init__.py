'''
Created on Jul 14, 2012

@author: boatkrap
'''


from flask import (Blueprint, render_template, request, redirect, make_response,
current_app, url_for, send_file)


from PIL import Image
import tempfile

from pumbaa import models

from .. import app
from . import photo_albums

default_prefix = '/photo_album'
module = Blueprint('photos', __name__, url_prefix='/photos')
app.register_blueprint(photo_albums.module, url_prefix=default_prefix)

 
@module.route('/<photo_album_id>/<photo_id>')
def view(photo_album_id, photo_id):
    
    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    photo = photo_album.get_photo(photo_id)
    
    extension = photo.image.filename[photo.image.filename.rfind('.')+1:]

    # if extension.lower() in ['jpg', 'jpeg']:
    #     response.content_type='image/jpeg'
    # elif extension.lower() in ['png']:
    #     response.content_type='image/png'
 
    img = Image.open(photo.image)
    img_format = img.format
    if photo.orientation == 'vertical':
        img = img.transpose(Image.ROTATE_90)
 
    tmp_img = tempfile.TemporaryFile()
             
    img.save(tmp_img, format=img_format)
    tmp_img.seek(0)
    
    return send_file(tmp_img,
                        attachment_filename=photo.image.filename,
                        as_attachment=True)
 
@module.route('/thumnail/<photo_album_id>/<photo_id>')
def thumbnail(photo_album_id, photo_id):

    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    photo = photo_album.get_photo(photo_id)
    
    extension = photo.image.filename[photo.image.filename.rfind('.')+1:]
    
    if photo.image.thumbnail:
        image = photo.image.thumbnail
        

    # if extension.lower() in ['jpg', 'jpeg']:
    #     response.content_type='image/jpeg'
    # elif extension.lower() in ['png']:
    #     response.content_type='image/png'
 
    
    img = Image.open(image)
    img_format = img.format
    
    if photo.orientation == 'vertical':
        img = img.transpose(Image.ROTATE_90)
 
    tmp_img = tempfile.TemporaryFile()
             
    img.save(tmp_img, format=img_format)
    tmp_img.seek(0)
 
    return send_file(tmp_img,
                        attachment_filename=photo.image.filename,
                        as_attachment=True)
