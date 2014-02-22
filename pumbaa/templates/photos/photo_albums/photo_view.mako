<%inherit file="/forums/base/base.mako"/>

<%block name="title">${photo_album.name + ": " + photo.get_image().filename}</%block>
<%block name="description">${photo.caption if len(photo.caption) > 0 else photo.get_image().filename}</%block>
<%block name="where_am_i">
<li><a href="${request.route_path('photos.photo_albums.index')}">Photo Albums</a></li>
<li><a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">${photo_album.name}</a></li>
</%block>
<%block name="panel_title">${photo_album.name}</%block>

<ul class="pager">
  <li class="previous${' disabled' if pprevious is None else ''}">
  	% if pprevious is not None:
  	<a href="${request.route_path('photos.photo_albums.photo_view', photo_album_id=photo_album.id, photo_id=pprevious.id)}">&larr; Previous</a>
  	% else:
  	<a href="#">&larr; Previous</a>
  	% endif
  </li>
  <li class="next${' disabled' if pnext is None else ''}">
  	% if pnext is not None:
  	<a href="${request.route_path('photos.photo_albums.photo_view', photo_album_id=photo_album.id, photo_id=pnext.id)}">Next &rarr;</a>
  	% else:
  	<a href="#">Next &rarr;</a>
  	% endif
  </li>
</ul>
<div class="row">
	<div class="col-sm-8 col-md-8 col-lg-9">
		<img class="img-rounded" alt="${photo.caption}" src="${request.route_path('photos.view', photo_album_id=photo_album.id, photo_id=photo.get_image().filename)}" width="100%" />
	</div>
	<div class="col-sm-4 col-md-4 col-lg-3">
		<div class="well well-sm">
			<div>
				<div class="pull-left" style="margin-right: 3px;">
					${photo.user.get_profile_picture() if photo.user.get_profile_picture() is not None else '' | n}
				</div>
				<div>
					${photo.user.get_display_name()}<br />
					${photo.created_date.strftime("%d %b %Y %X")}
				</div>
			</div>
			<p><b>License:</b> ${photo.license}</p>
			% if photo.caption:
			<p>${photo.caption}</p>
			% endif
		</div>
	</div>
</div>
<%block name="more_body">
<%include file="/base/comments.mako", args="item=photo"/>
</%block>