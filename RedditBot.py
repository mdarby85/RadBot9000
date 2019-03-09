import praw
import config
import os

def bot_login():
    print ("Logging in...")
    reddit = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "RadBot9000 v0.1")
    print ("Logged in!")
    return reddit

def run_bot(reddit):
    processed = []

    for submission in reddit.subreddit('2Rad4Radio').new(limit = 5):
        with open("/home/matt/Bots/RadBot/replied.txt", "r") as f:
            processed = f.read()
            processed = processed.split("\n")
            processed = list(filter(None, processed))
        if submission.id not in processed:
            submission.reply('Rad').mod.distinguish(sticky=True)
            processed.append(submission.id)
            with open("/home/matt/Bots/RadBot/replied.txt", "w") as f:
                for post_id in processed:
                    f.write(post_id + "\n")

reddit = bot_login()
run_bot(reddit)
