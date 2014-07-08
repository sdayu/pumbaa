<%! 
	import pumbaa
	from pumbaa import models
	from pyramid.security import has_permission
%>
	<div class="navbar navbar-default navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="${request.route_path('index')}">Pumbaa</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
          	<% is_active = False %>
          	% for check_str in ['forums']:
	            % if check_str in request.current_route_path():
	            <li class="active">
	             <% is_active = True %>
	            % endif
            % endfor
            % if not is_active:
            <li>
            % endif
            	<a href="${request.route_path('forums.index')}">Forums</a>
            </li>
            <li>
            	<a href="${request.route_path('calendars.calendars.index')}">Calendar</a>
            </li>
            <li>
            	<a href="${request.route_path('forums.topics.compose')}">New Topic</a>
            </li>
            
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Addition <b class="caret"></b></a>
              <ul class="dropdown-menu">
              	<li><a href="${request.route_path('index')}">หน้าแรก</a></li>
              	<li><a href="${request.route_path('forums.topics.index')}">Topics</a></li>
              	<li><a href="${request.route_path('photos.photo_albums.index')}">Photo Albums</a></li>
  				<li><a href="${request.route_path('calendars.calendars.index')}">Calendar</a></li>
  				<li><a href="${request.route_path('calendars.calendars.agenda')}">Agenda</a></li>
  				<li><a href="${request.route_path('forums.tags.index')}">Tags</a></li>
  				<li><a href="${request.route_path('planet')}">Planet (beta)</a></li>
                <li class="divider"></li>
           		<li><a href="${request.route_path('pages.view', title='About')}">About</a></li>
            	<li><a href="${request.route_path('pages.view', title='Contact')}">Contact</a></li>
                <li class="dropdown-header">Pumbaa</li>
                <li><a href="https://github.com/sdayu/pumbaa">Version ${pumbaa.__version__}</a></li>
              </ul>
            </li>
          </ul>

          % if request.user:
          <ul class="nav navbar-nav navbar-right">
          	<li>
          		<a href="${request.route_path('home')}" title="${request.user.username}">
          			% if request.user.get_profile_picture():
          				${request.user.get_profile_picture(20) | n}
          			% else:
          				${request.user.username}
          			% endif
          		</a>
          	</li>
          	<li class="dropdown">
          		<a href="#" class="dropdown-toggle" data-toggle="dropdown"><b><span class="glyphicon glyphicon-cog"></span></b></a>
				<ul class="dropdown-menu">
					<li>
		          		<a href="${request.route_path('home')}">Home</a>
		            </li>
		            <li>
		          		<a href="${request.route_path('manager.users.approve')}">Approve users 
		          		<%
		          			wait_users = models.User.objects(status='wait for approval', approvers__user__ne=request.user).count()
		          		%>
		          		% if wait_users > 0:
		          			<span class="badge">${wait_users}</span>
		          		% endif
		          		</a>
		            </li>
					<li>
		            	<a href="${request.route_path('forums.topics.compose')}">New topic</a>
		            </li>
		            <li>
		            	<a href="${request.route_path('manager.photo_albums.create')}">New photo albums</a>
		            </li>
		            <li>
		            	<a href="${request.route_path('manager.events.create')}">New events</a>
		            </li>
		            <li>
		            	<a href="${request.route_path('manager.topics.index')}">My topics</a>
		            </li>
		            % if has_permission('admin', request.context, request):
		            <li class="divider"></li>
		            <li>
		            	<a href="${request.route_path('admin.index')}">Administrator</a>
		            </li>
		            % endif
		            <li class="divider"></li>
	            	<li><a href="${request.route_path('logout')}">Log out</a></li>
              	</ul>
          	</li>
          </ul>
          % else:
          	<form class="navbar-form navbar-right" action="${request.route_path('login')}">
            	<button type="submit" class="btn btn-primary">
            		<b>Login</b>
            	</button>
          	</form>
          % endif
          
        </div><!--/.nav-collapse -->
      </div>
    </div>
