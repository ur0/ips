import markovify
import sys

# Open the corpus
with open(sys.argv[1], "r") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)
print("Model ready!")

# Dump the model to disk
model_json = text_model.to_json()
with open(sys.argv[2], "w+") as out:
    out.write(model_json)
