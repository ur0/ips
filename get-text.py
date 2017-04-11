import praw
import sys

reddit = praw.Reddit("ips", user_agent="Indian People Simulator by u/ur_0")
sources = []
sources += reddit.subreddit("theunkillnetwork").top("all", limit=200)
sources += reddit.subreddit("india").top("all", limit=200)
sources += reddit.subreddit("bakchodi").top("all", limit=200)
sources += reddit.subreddit("indiaspeaks").top("all", limit=200)

with open(sys.argv[1], "w+") as f:
    for post in sources:
            f.write(post.selftext.encode("utf-8").strip())
            f.write("\n")
            post.comments.replace_more(limit=0)
            for comment in post.comments.list():
                f.write(comment.body.encode("utf-8").strip())
                f.write("\n")
