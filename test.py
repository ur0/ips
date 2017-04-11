import markovify
import sys

reddit = praw.Reddit("ips", user_agent="Indian People Simulator by /u/ur_0")
if len(sys.argv) is not 2:
    print("Need one argument - location of the model JSON.")
    exit(-1)

model_json = open(sys.argv[1]).read()
model = markovify.Text.from_json(model_json)

for c in range(0,5):
    text = model.make_sentence()
    text += "\r\n\r\n*****\r\n\r\nThis is a bot. Contact /u/ur_0 for help."
    print(text)
