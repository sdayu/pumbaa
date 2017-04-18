
from .. import app


from flask import Blueprint, render_template
from flask_login import login_required
from flask_principal import Permission, RoleNeed


from . import topics

default_prefix = '/dashboard'
module = Blueprint('dashboard', __name__, url_prefix=default_prefix)
app.register_blueprint(topics.module, url_prefix=default_prefix+'/topics')




@module.route('/')
@login_required
def index():
    return render_template('/dashboard/index.jinja2')
