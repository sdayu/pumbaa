'''
Created on Nov 10, 2013

@author: boatkrap
'''


from flask import Blueprint, render_template, request, redirect, make_response, current_app, url_for

from pumbaa import models, forms


module = Blueprint('photos.photo_albums', __name__, url_prefix='/photo_albums')

# @view_config(route_name='photos.photo_albums.index',
#              renderer='/photos/photo_albums/index.mako')
@module.route('/')
def index():
    photo_albums = models.PhotoAlbum.objects(status="publish").all()
    return render_template('/photos/photo_albums/index.jinja2',
                photo_albums=photo_albums
                )

# @view_config(route_name='photos.photo_albums.view',
#              renderer='/photos/photo_albums/view.mako')
@module.route('/<photo_album_id>')
def view(photo_album_id):
    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    return render_template('/photos/photo_albums/view.jinja2',
                photo_album=photo_album
                )
    
# @view_config(route_name='photos.photo_albums.photo_view',
#              renderer='/photos/photo_albums/photo_view.mako')
@module.route('/<photo_album_id>/<photo_id>')
def photo_view(photo_album_id, photo_id):
    
    photo_album = models.PhotoAlbum.objects.with_id(photo_album_id)
    photo, pprevious, pnext = photo_album.get_photo_index(photo_id)
    return render_template('/photos/photo_albums/photo-view.jinja2',
                photo_album=photo_album,
                photo=photo,
                pprevious=pprevious,
                pnext=pnext
                )

# @view_config(route_name='photos.photo_albums.comment') 
# @view_config(route_name='photos.photo_albums.photo_comment')

@module.route('/comments/<photo_album_id>/<photo_id>')
@module.route('/comments/<photo_album_id>')
def photo_comment(photo_album_id, photo_id=None):
   
    # photo_album_id = request.matchdict.get('photo_album_id')
    # photo_id = request.matchdict.get('photo_id', None)
    
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
