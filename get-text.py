import praw
import sys

reddit = praw.Reddit("ips", user_agent="Indian People Simulator by u/ur_0")
sources = []
sources += reddit.subreddit("theunkillnetwork").top("all")
sources += reddit.subreddit("india").top("all")
sources += reddit.subreddit("bakchodi").top("all")
sources += reddit.subreddit("indiaspeaks").top("all")

with open(sys.argv[1], "w+") as f:
    for post in sources:
            f.write(post.selftext)
            f.write("\n")
