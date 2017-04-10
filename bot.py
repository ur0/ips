import praw
import markovify
import sys
import time

reddit = praw.Reddit("ips", user_agent="Indian People Simulator by /u/ur_0")
model_json = open(sys.argv[1]).read()
model = markovify.Text.from_json(model_json)

for c in reddit.subreddit("all").stream.comments():
    if "+indianpeoplesim" in c.body or "+ips" in c.body:
        text = model.make_sentence()
        text += "\r\n\r\nThis is a bot. Contact /u/ur_0 for help."
        try:
            c.reply(text)
            print("Replied to a comment.")
        except praw.exceptions.APIException as e:
            print("API error, sleeping 10 minutes.")
            time.sleep(600)
            try:
                c.reply(text)
            except praw.exceptions.APIException as e:
                print("Persistent API errors, not bothering to reply to this.")

