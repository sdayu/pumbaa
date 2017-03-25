__version__ = '1.0.1'


from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import user_logged_in
from flask_principal import Principal, Permission, RoleNeed
from flask_login import LoginManager
from flask_iniconfig import INIConfig

app = Flask(__name__)
# app.config.from_pyfile('../development.cfg')
# app.secret_key = 'super secret key'

# load extension
# db = MongoEngine(app)

# intial login
login_manager = LoginManager(app)

# initial principal
principals = Principal(app)
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

from . import aaa_setup

from authomatic import Authomatic
from .authomatic_config import CONFIG
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)
from .views import *


# print(app.url_map)
# from .views import dashboard
# from .views import admin

# from .views import literatures

# app.register_blueprint(site.module)
# app.register_blueprint(forums.module)
# app.register_blueprint(dashboard.module, url_prefix='/dashboard')
# app.register_blueprint(literatures.novels.module, url_prefix='/novels')
# app.register_blueprint(literatures.stories.module, url_prefix='/stories')
# app.register_blueprint(admin.module, url_prefix='/admin')




import optparse
import os

def get_program_options(default_host='127.0.0.1',
        default_port='5000'):

    """
    Takes a flask.Flask instance and runs it. Parses 
    command-line flags to configure the app.
    """

    # Set up the command-line options
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)

    # Two options useful for debugging purposes, but 
    # a bit dangerous so not exposed in the help message.
    parser.add_option("-c", "--config",
                      dest="config",
                      help=optparse.SUPPRESS_HELP, default=None)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)
    parser.add_option("-p", "--profile",
                      action="store_true", dest="profile",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    # If the user selects the profiling option, then we need
    # to do a little extra setup
    if options.profile:
        from werkzeug.contrib.profiler import ProfilerMiddleware

        app.config['PROFILE'] = True
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app,
                       restrictions=[30])
        options.debug = True

    return options

def initial():
    options = get_program_options()
    config_file = os.path.abspath(options.config)
    
    if config_file:
        INIConfig(app)
        app.config.from_inifile(config_file)
    db = MongoEngine(app)

initial()
