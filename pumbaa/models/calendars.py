class Event(me.Document):
    meta = {'collection' : 'events'}
    
    title = me.StringField(required=True)
    description = me.StringField(required=True)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField()
    
    status = me.StringField(required=True, default='draft')
    """ status: draft, publish, delete """
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')

    author = me.ReferenceField("User", dbref=True, required=True)

    tags = me.ListField(me.StringField(required=True), required=True) 
	events = me.StringField(require=True, default='department', choices=['department', 'conference', 'thesis', 'student'])
