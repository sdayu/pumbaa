'''
Created on Nov 9, 2013

'''

import mongoengine as me

import datetime
import bson

from . import forums

class Photo(me.EmbeddedDocument):
    id = me.ObjectIdField(required=True, default=bson.ObjectId)
    
    caption = me.StringField()
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)

    image = me.ImageField(collection_name='images',
                          size=(1024, 786, True),
                          thumbnail_size=(320, 240, True),
                          )
    comments = me.ListField(me.EmbeddedDocumentField(forums.Comment))
    
class PhotoAlbum(me.Document):
    meta = {'collection' : 'photo_albums'}
    
    name = me.StringField(required=True)
    description = me.StringField()
    photos = me.ListField(me.EmbeddedDocumentField(Photo))
    status = me.StringField(required=True, default='draft')
    """ status: draft, publish, delete """
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    
    comments = me.ListField(me.EmbeddedDocumentField(forums.Comment))

    def get_photo(self, photo_id):
        for photo in self.photos:
            if photo.image.filename == photo_id:
                return photo
            if str(photo.id) == photo_id:
                return photo