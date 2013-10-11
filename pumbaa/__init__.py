from pyramid.config import Configurator

from . import routes
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    routes.add_route(config)
    config.scan()

    return config.make_wsgi_app()
