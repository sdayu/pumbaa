from flask import Blueprint, render_template
from flask_login import login_required
from flask_principal import Permission, RoleNeed


from . import topics

url_prefix = '/dashboard'
module = Blueprint('dashboard', __name__, url_prefix=url_prefix)


def register_blueprint(app):
    app.register_blueprint(module)

    for view in [topics]:

        if 'register_blueprint' in dir(view):
            view.register_blueprint(app, url_prefix)
        else:
            app.register_blueprint(
                view.module,
                url_prefix=url_prefix + view.module.url_prefix)



@module.route('/')
@login_required
def index():
    return render_template('/dashboard/index.jinja2')
