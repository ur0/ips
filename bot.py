import praw
import markovify
import sys
import time

reddit = praw.Reddit("ips", user_agent="Indian People Simulator by /u/ur_0")
if len(sys.argv) is not 2:
    print("Need one argument - location of the model JSON.")
    exit(-1)

model_json = open(sys.argv[1]).read()
model = markovify.Text.from_json(model_json)

for c in reddit.subreddit("all").stream.comments():
    if "+indianpeoplesim" in c.body or "+ips" in c.body:
        print("Comment from", c.author.name)
        text = ""
        while len(text) == 0:
            new = model.make_sentence(tries=100)
            if not isinstance(new, type(None)):
                text += new
        text += "\r\n\r\n*****\r\n\r\nThis is a bot. Contact /u/ur_0 for help. [Source code](https://github.com/ur0/ips)."
        try:
            c.reply(text)
            print("Replied successfully")
        except praw.exceptions.APIException as e:
            print("API error, sleeping 10 minutes")
            time.sleep(600)
            try:
                print("Attempting to dispatch rate-limited message")
                c.reply(text)
            except praw.exceptions.APIException as e:
                print("Persistent API errors, not bothering to reply to this")

