<%inherit file="/forums/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="title">Photo Albums</%block>
<%block name="where_am_i">
<li><a href="${request.route_path('photos.photo_albums.index')}">Photo Albums</a></li>
</%block>
<%block name="panel_title">Photo Albums</%block>

<div class="row">
% for photo_album in photo_albums:
  <div class="col-sm-6 col-md-3 col-lg-2">
    <div class="thumbnail">
      <a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">
      	<img src="${request.route_path('photos.thumbnail', photo_album_id=photo_album.id, photo_id=photo_album.photos[0].image.filename)}" alt="${photo_album.name}">
      </a>
      <div class="caption">
        <h3>${photo_album.name}</h3>
        <p>${photo_album.description}</p>
        <p><a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}" class="btn btn-primary" role="button">ชมภาพ</a></p>
      </div>
  </div>
% endfor
</div>