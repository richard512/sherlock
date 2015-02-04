# -*- coding: utf-8 -*-
try:
	from sub_data import subreddits
except:
	pass

subreddits_dict = dict((subreddit['name'], subreddit) for subreddit in subreddits)

ignore_text_subs = [s["name"] for s in subreddits if s["ignore_text"]=="Y"]

default_subs = [s["name"] for s in subreddits if s["default"]=="Y"]
