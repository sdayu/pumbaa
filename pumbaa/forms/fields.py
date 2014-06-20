from wtforms import fields, widgets

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