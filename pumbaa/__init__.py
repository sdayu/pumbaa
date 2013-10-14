from pyramid.config import Configurator

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pumbaa import models

from pumbaa.routes import add_routes
from pumbaa.security import group_finder

def main(global_config, **settings):
    authn_policy = AuthTktAuthenticationPolicy(settings.get('pumbaa.secret'), callback=group_finder)
    authz_policy = ACLAuthorizationPolicy()
    
    config = Configurator(settings=settings, 
                          root_factory='pumbaa.acl.RootFactory',
                          authentication_policy=authn_policy, 
                          authorization_policy=authz_policy)

    models.initial(settings)
    
    add_routes(config)
    config.scan('pumbaa.views')
    
    from .security import RequestWithUserAttribute
    config.set_request_factory(RequestWithUserAttribute)

    return config.make_wsgi_app()