from .. import app

from . import site
from . import accounts
from . import forums
from . import photos

app.register_blueprint(site.module)
app.register_blueprint(accounts.module)
app.register_blueprint(forums.module)
app.register_blueprint(photos.module)
