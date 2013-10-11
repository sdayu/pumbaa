'''
Created on Oct 11, 2013

@author: boatkrap
'''


def add_route(config):
    config.add_route('home', '/')
    
    config.add_static_view('public', 'public', cache_max_age=3600)
    