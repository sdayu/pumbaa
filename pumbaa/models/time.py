import datetime

import mongoengine as me

class PumbaaTime:
    def getTime(self):
        return datetime.datetime.now()


