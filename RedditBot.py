import praw
import config

def bot_login():
    print "Logging in..."
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "RadBot9000 v0.1")
    print "Logged in!"
    return r

def run_bot(r):
    processed = []
    for submission in r.subreddit('2Rad4Radio').new(limit = 5):
        if submission.id not in processed:
            submission.reply("Rad")


r = bot_login()
run_bot(r)
