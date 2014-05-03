'''
Created on May 3, 2014

@author: Mildronize (Thada Wangthammang)
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models

@view_config(route_name='feeds', renderer="/feed/index.mako")
def index(request):
    # tags = models.Topic.objects.distinct('tags')
    print("testing")
    return {'project': 'feed feature'}