import markovify
import sys

if len(sys.argv) is not 2:
    print("Need one argument - location of the model JSON.")
    exit(-1)

model_json = open(sys.argv[1]).read()
model = markovify.Text.from_json(model_json)

for c in range(0,5):
    text = ""
    while len(text) == 0:
        new = model.make_sentence(tries=1000)
        if not isinstance(new, type(None)):
            text += new
    text += "\r\n\r\n*****\r\n\r\nThis is a bot. Contact /u/ur_0 for help."
    print(text)
