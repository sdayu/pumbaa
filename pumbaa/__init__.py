__version__ = '0.1.3'

from pyramid.config import Configurator

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from pyramid_beaker import session_factory_from_settings

from pumbaa import models
from pumbaa.routes import add_routes
from pumbaa.acl import group_finder

def main(global_config, **settings):
    authn_policy = AuthTktAuthenticationPolicy(settings.get('pumbaa.secret'), callback=group_finder)
    authz_policy = ACLAuthorizationPolicy()
    pumbaa_session_factory = session_factory_from_settings(settings)
    
    config = Configurator(settings=settings, 
                          root_factory='pumbaa.acl.RootFactory',
                          authentication_policy=authn_policy, 
                          authorization_policy=authz_policy,
                          session_factory = pumbaa_session_factory)

    models.initial(settings)
    
    config.include('velruse.providers.facebook')
    config.add_facebook_login_from_settings(prefix='velruse.facebook.')
    config.include('velruse.providers.google_oauth2')
    config.add_google_oauth2_login_from_settings(prefix='velruse.google.')
    config.include('velruse.providers.twitter')
    config.add_twitter_login_from_settings(prefix='velruse.twitter.')
    
    add_routes(config)
    config.scan('pumbaa.views')
    
    from .request_factory import RequestWithUserAttribute
    config.set_request_factory(RequestWithUserAttribute)

    return config.make_wsgi_app()
