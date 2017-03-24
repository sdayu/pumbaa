__version__ = '1.0.1'


from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import user_logged_in
from flask_principal import Principal, Permission, RoleNeed
from flask_login import LoginManager
from flask_appconfig import AppConfig

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


def initial(app, config_file=None):
    if config_file:
        AppConfig(app, config_file)
    db = MongoEngine(app)
