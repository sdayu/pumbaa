
from .. import app

from . import topics

from flask import Blueprint


default_prefix = '/dashboard'
module = Blueprint('dashboard', __name__, url_prefix=default_prefix)
app.register_blueprint(topics.module, url_prefix=default_prefix+'/topics')

