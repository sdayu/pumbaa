from datetime import datetime, timedelta 
from pumbaa import models
    

def tooltip_get_days(uptime, diff_time):

	if diff_time.days < 0:
		return "???"
	if diff_time.days < 1:
		return tooltip_get_times(diff_time.seconds)
	elif diff_time.days < (1*2):
		return "%d day" % (diff_time.days)
	elif diff_time.days < 7:
		return "%d days" % (diff_time.days)
	elif diff_time.days < (7*2):
		return "%d week" % (diff_time.days/7)
	else:
		return uptime.strftime("%b %d, %Y")

def tooltip_get_times(times):
	if times < (1*2):
		return "1 sec"
	elif times < 60:
		return "%d secs" % (times)
	elif times < (60*2):
		return "%d min" % (times/60)
	elif times < (60*60):
		return "%d mins" % (times/60)
	elif times < (60*60*2):
		return "%d hr" % (times/3600)
	else:
		return "%d hrs" % (times/3600)

def topic_diff_time(topic):
    topic_timenow  = datetime.now()
    topic_timediff = topic_timenow - topic.updated_date

    return topic_timediff

def get_current_time():
    return datetime.now()

def get_forum(forum_name):
    return models.Forum.get_forum(forum_name)
