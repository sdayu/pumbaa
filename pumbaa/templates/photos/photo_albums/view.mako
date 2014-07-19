<%inherit file="/forums/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="title">${photo_album.name}</%block>
<%block name="description">${photo_album.description}</%block>
<%block name="where_am_i">
<li><a href="${request.route_path('photos.photo_albums.index')}">Photo Albums</a></li>
<li class="active">${photo_album.name}</li>
</%block>
<%block name="panel_title">${photo_album.name}</%block>

<div style="padding: 5px;">
	<p class="text-primary">
		${photo_album.description}
	</p>
	% if hasattr(photo_album, 'event_date') and photo_album.event_date is not None:
	<p class="text-primary">
		เหตุการณ์นี้เกิดขึ้นเมื่อ ${photo_album.event_date.date()}
	</p>
	% endif
</div>

% for photo in photo_album.photos:
	<a href="${request.route_path('photos.photo_albums.photo_view', photo_album_id=photo_album.id, photo_id=photo.id)}" >
		<img class="img-thumbnail" style="${'width:200px;' if photo.orientation == 'horizontal' else 'height:150px;'}" alt="${photo.caption}" src="${request.route_path('photos.thumbnail', photo_album_id=photo_album.id, photo_id=photo.image.filename)}" />
	</a>
% endfor

<%block name="more_body">
<%include file="/base/comments.mako", args="item=photo_album" />
</%block>
