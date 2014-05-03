from pyramid.view import view_config
from pumbaa import models

@view_config(route_name='profile.index', renderer='/profile/index.mako')
def index(request):
    profile_id = request.matchdict['profile_id']
    
    user = models.User.objects(username=profile_id).first()
    
    return dict(
                profile_id=user.username
                )
