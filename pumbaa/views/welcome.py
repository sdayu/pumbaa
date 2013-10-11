from pyramid.view import view_config


@view_config(route_name='home', renderer='/welcome/welcome.mako')
def my_view(request):
    return {'project': 'pumbaa'}
