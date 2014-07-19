<%inherit file="/forums/base/base.mako"/>
<%! 
	from pumbaa import models 
	import math
%>
<%block name="title">Photo Albums</%block>
<%block name="description">Photo Albums: ${", ".join([photo_album.name for photo_album in photo_albums])}</%block>
<%block name="where_am_i">
<li class="active">Photo Albums</li>
</%block>
<%block name="panel_title">Photo Albums</%block>
<%
count = 0
album_count = photo_albums.count()
%>
% for i in range(0, math.ceil(album_count/4)+1):
<div class="row">
  % for i in range(0, 4):
  <%
  	if count >=  album_count:
  		break
  	photo_album = photo_albums[count] 
  %>
  % if len(photo_album.photos) > 0:
  <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
    <div class="thumbnail">
      <a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">
      	<img src="${request.route_path('photos.thumbnail', photo_album_id=photo_album.id, photo_id=photo_album.photos[0].image.filename)}" alt="${photo_album.name}" width="100%">
      </a>
      <div class="caption">
        <h3 style="word-wrap:break-word;">${photo_album.name}</h3>
        <p>${photo_album.description}</p>
        <p><a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}" class="btn btn-primary" role="button">ชมภาพ</a></p>
      </div>
     </div>
  </div>
  % endif
  <% count += 1 %>
  % endfor
</div>
% endfor