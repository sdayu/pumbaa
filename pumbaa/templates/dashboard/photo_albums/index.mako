<%inherit file="/manager/base/base.mako"/>
<%block name="title">
Photo Album Manager
</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Photo Albums</a></li>
</%block>
<%block name="panel_title">Photo Albums</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('manager.photo_albums.create')}">New Photo Album</a></li>
</ul>

% if len(my_photo_albums) > 0:
<h4 class="bg-primary">My Photo Albums</h4>
<ul class="list-group">
	% for photo_album in my_photo_albums:
    <li class="list-group-item">
    	<a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">
    		${photo_album.name} ${'<span class="glyphicon glyphicon-share"></span>' if photo_album.shared else '' | n}
    	</a> 
    		:: 
    	<a href="${request.route_path('manager.photo_albums.add_photo', photo_album_id=photo_album.id)}">add photo</a>
    	<div class="pull-right">
    		<a href="${request.route_path('manager.photo_albums.edit', photo_album_id=photo_album.id)}" title="Edit photo album"><span class="glyphicon glyphicon-edit"></span></a> 
    		<a href="${request.route_path('manager.photo_albums.delete', photo_album_id=photo_album.id)}" title="Delete photo album"><span class="glyphicon glyphicon-remove"></span></a>
    	</div>
    	
    </li>
    % endfor
</ul>
% endif 

% if len(share_photo_albums) > 0:
<h4 class="bg-primary">Share Photo Albums</h4>
<ul class="list-group">
	% for photo_album in share_photo_albums:
    <li class="list-group-item">
    	<a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">${photo_album.name}</a> :: 
    	<a href="${request.route_path('manager.photo_albums.add_photo', photo_album_id=photo_album.id)}">add photo</a>
    </li>
    % endfor
</ul>
% endif