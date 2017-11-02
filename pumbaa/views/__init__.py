
from . import site
from . import accounts
from . import forums
from . import photos
from . import dashboard

def register_blueprint(app):
    for view in [site,
                 accounts,
                 forums,
                 photos,
                 dashboard]:
        if 'register_blueprint' in dir(view):
            view.register_blueprint(app)
        else:
            app.register_blueprint(view.module)

