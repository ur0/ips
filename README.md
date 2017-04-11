# Indian People Simulator

This is a Reddit bot which uses Markov chains to analyze the top 200 posts and comments on Indian subreddits and replies with a generated sentence based on the aforementioned model eveytime it is invoked.

This is a fun project and is not intended to hurt or defame any individual or community.

## Setting up
This requires Python (2.7 - 3.6.0 were tested). You must install all requirements as listed in `requirements.txt` and create a `praw.ini` file in the project root with the following content.

```
[ips]
client_id=xyzxyz
client_secret=jeqlkjklaxxz
username=indianpeoplesim
password=hunter2
```

Be sure to replace above values with your credentials.

## Actually making the bot run
1. Gather the top posts and replies using `python get-text.py somefile.posts`.
2. Create the model using `python read-corpus.py somefile.posts model.json`.
3. Start the Reddit bot using `python bot.py model.json`

## License
Licensed under the MIT license, see the `LICENSE` file for details.
