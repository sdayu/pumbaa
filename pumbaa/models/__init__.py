from flask_mongoengine import MongoEngine

from .users import User, Role, Profile, Approver
from .forums import Topic, Comment, Forum, TopicHistory
from .photos import PhotoAlbum, Photo
from .events import Event


db = MongoEngine()

def init_db(app):
    db.init_app(app)
