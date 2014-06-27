from wtforms import fields, widgets

import datetime

class TagListField(fields.Field):
    widget = widgets.TextInput()

    def _value(self):
        if self.data:
            return ', '.join(self.data)
        else:
            return ''

    def process_formdata(self, valuelist):
        data = []
        if valuelist:
            data = [tag.strip() for tag in valuelist[0].split(',') if len(tag.strip()) > 0]
        self.data = data
        
class DateNoneField(fields.DateField):
    def __init__(self, label=None, validators=None, format='%Y-%m-%d', **kwargs):
        super(DateNoneField, self).__init__(label, validators, format, **kwargs)

    def process_formdata(self, valuelist):
        if valuelist and len(valuelist) > 0 and len(valuelist[0]) > 0:
            date_str = ' '.join(valuelist)
            try:
                self.data = datetime.datetime.strptime(date_str, self.format).date()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid date value'))