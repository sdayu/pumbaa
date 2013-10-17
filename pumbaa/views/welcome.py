from pyramid.view import view_config


@view_config(route_name='index', renderer='/welcome/index.mako')
def index(request):
    return {}
