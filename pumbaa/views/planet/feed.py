'''
Created on May 3, 2014

@author: Mildronize (Thada Wangthammang)
'''

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pumbaa import models
import re
import random

import feedparser
from time import mktime
from datetime import datetime

@view_config(route_name='planet', renderer="/planet/index.mako")
def index(request):
	#print("testing")
	users = models.User.objects()
	results = []
	for user in users:
		if hasattr(user,'feed_url') == False:
			continue
		if user.feed_url is None:
			continue
		# print(user.username)
		if "http://" not in user.feed_url and "https://" not in  user.feed_url:
			continue
		data = feedparser.parse(user.feed_url)

		for post in data.entries:

			plaintext = striphtml(post.content[0].value)
			dt = datetime.fromtimestamp(mktime(post.published_parsed))

			results.append({
				'title' : post.title,
				'link' : post.link,
				'published' : dt,
				'published_day' : show_day(dt),
				'published_month' : show_month(dt),
				'published_year' : show_year(dt),
				'content' : plaintext[0:200] + ' ...',
				'img_src' : get_image_url(post.content[0].value)
				})
	results = sorted(results, key=lambda k: k['published'], reverse=True) 
	return {'project': 'feed feature', 'results': results}
   
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)
def get_image_url(data):
	no_image_url = "/public/images/no-image.jpg"
	matches = re.findall('src="([^"]+)"',data)
	if matches:
		return matches[random.randint(0, len(matches)-1)]
	else:
		return no_image_url
def show_year(data):
	return '{0:%Y}'.format(data)
def show_month(data):
	return '{0:%b}'.format(data)
def show_day(data):
	return '{0:%d}'.format(data)

	
