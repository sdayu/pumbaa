'''
Created on Oct 20, 2013

@author: boatkrap
'''
from feedformatter import Feed
from pyramid.view import view_config
from pyramid.response import Response

from pumbaa import models

import datetime

@view_config(route_name="feeds")
@view_config(route_name="feeds.forums")
def feed(request):
    
    forum_name = request.matchdict.get('forum_name', None)
    
    if forum_name:
        forum = models.Forum.objects(name__iexact=forum_name).first()
        topics = models.Topic.objects(status='publish', tags__in=forum.tags).order_by("-published_date").limit(10)
    else:
        topics = models.Topic.objects(status='publish').order_by("-published_date").limit(10)

    # Create the feed
    feed = Feed()
    
    # Set the feed/channel level properties
    feed.feed["title"] = "Pumbaa feed"
    feed.feed["link"] = request.current_route_url()
    feed.feed["author"] = {'name' : "pumbaa"}
    feed.feed["description"] = "Pumbaa feed"
    feed.feed["update"] = datetime.datetime.now()
    
    for topic in topics:
        # Create an item
        item = {}
        item['title'] = topic.title
        item['link'] = request.route_url('forums.topics.view', topic_id=topic.id, title=topic.title)
        item['description'] = topic.description
        item['pubDate'] = topic.published_date
        item['guid'] = request.route_url('forums.topics.view', topic_id=topic.id, title=topic.title)
        item['category'] = ", ".join(topic.tags)
        item['author'] = {'name' : topic.author.username}
        
        # Add item to feed
        feed.items.append(item)
    
    return Response(feed.format_atom_string())