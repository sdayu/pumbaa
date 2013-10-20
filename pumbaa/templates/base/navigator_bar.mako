<%! import pumbaa %>
	<div class="navbar navbar-inverse navbar-fixed-top">
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
          	% for check_str in ['home', 'manager', 'admin']:
	            % if check_str in request.current_route_path():
	            <li class="active">
	             <% is_active = True %>
	            % endif
            % endfor
            % if not is_active:
            <li>
            % endif
            	<a href="${request.route_path('home')}">Home</a>
            </li>
            % if request.user:
            <li><a href="${request.route_path('logout')}">Logout</a></li>
            % else:
            <li><a href="${request.route_path('login')}">Login</a></li>
            % endif
            
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Addition <b class="caret"></b></a>
              <ul class="dropdown-menu">
              	<li><a href="${request.route_path('pages.view', title='About')}">About</a></li>
            	<li><a href="${request.route_path('pages.view', title='Contact')}">Contact</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Pumbaa</li>
                <li><a href="#">Version ${pumbaa.__version__}</a></li>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>