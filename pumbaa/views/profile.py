from pyramid.view import view_config
from pumbaa import models

@view_config(route_name='profile.index', renderer='/profile/index.mako')
def index(request):
    profile_name="Zero"
    
    return dict(
                profile_name=profile_name
                )
