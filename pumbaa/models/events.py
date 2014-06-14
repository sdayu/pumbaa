import mongoengine as me
import datetime

from .forums import Topic

EVENT_TYPES = ['undergraduate', 'graduate', 'department', 'conference', 'thesis', 'other']

class RepeatableEvent(me.EmbeddedDocument):
    pass
    

class Event(me.Document):
    meta = {'collection': 'events'}

    topic = me.ReferenceField(Topic, required=True, dbref=True)
    status = me.StringField(required=True, default='draft')
    """ status: draft, publish, delete """

    started_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    ended_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    venue = me.StringField()
    
    all_day = me.BooleanField(required=True, default=False)
    repeat = me.EmbeddedDocumentField(RepeatableEvent)

    ip_address = me.StringField(max_length=100, required=True, default='0.0.0.0')

    author = me.ReferenceField("User", dbref=True, required=True)

    tags = me.ListField(me.StringField(required=True), required=True) 
    event_type = me.StringField(required=True, default='department', choices=EVENT_TYPES)
    
    def is_repeatable(self):
        repeat = False
        if self.repeat is not None:
            repeat = True
            
        return repeat