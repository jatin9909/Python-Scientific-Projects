import praw
import config
import time
import csv
import random
import os

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Bollywood-bot v1.0")
	print("Logged in!")

	return r

def top_post_from_subreddit(r):
	subreddit = r.subreddit('india')
	top_post=[]
	for submission in r.subreddit('IndiaSpeaks').top(limit=20):
		top_post.append(submission.title)
		for i in range(0,19):
			try:
				print(submission.comments[i].body)
				with open("comments_right.txt","a") as f:
					f.write(submission.comments[i].body+"\n\n")
			except UnicodeEncodeError:
				pass		
	return top_post	


r = bot_login()
posts = top_post_from_subreddit(r)
print(posts)
