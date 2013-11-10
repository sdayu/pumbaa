<%inherit file="/manager/base/base.mako"/>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Photo Albums</a></li>
</%block>
<%block name="panel_title">Photo Albums</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('manager.photo_albums.create')}">New Photo Album</a></li>
</ul>
<ul class="list-group">
	% for photo_album in photo_albums:
    <li class="list-group-item">
    	<a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">${photo_album.name}</a> :: 
    	<a href="${request.route_path('manager.photo_albums.add_photo', photo_album_id=photo_album.id)}">add photo</a>
    </li>
    % endfor
</ul>