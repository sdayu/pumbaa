from mongoengine import connect

from .users import User, Role, Profile

def initial(settings):
    connect(settings.get('mongodb.db_name'), host=settings.get('mongodb.host'))