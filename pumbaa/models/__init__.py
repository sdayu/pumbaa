from mongoengine import connect

def initial(settings):
    connect(settings.get('mongodb.db_name'), host=settings.get('mongodb.host'))