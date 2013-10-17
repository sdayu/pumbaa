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
            <li class="active"><a href="${request.route_path('home')}">Home</a></li>
            % if request.user:
            <li><a href="${request.route_path('logout')}">Logout</a></li>
            % else:
            <li><a href="${request.route_path('login')}">Login</a></li>
            % endif
            
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Addition <b class="caret"></b></a>
              <ul class="dropdown-menu">
              	<li><a href="#about">About</a></li>
            	<li><a href="#contact">Contact</a></li>
            	<%doc>
                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
                </%doc>
              </ul>
            </li>
            
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>