from mongoengine import connect

from .users import User, Role, Profile, Approver

def initial(settings):
    connect(settings.get('mongodb.db_name'), host=settings.get('mongodb.host'))