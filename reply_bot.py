import praw
import pdb
import re
import os
import random

# Reddit instance 
reddit = praw.reddit('bot1') #added the required values in praw.ini file inside the venv directory.
#[bot1]
#username = ""
#password = ""
#secret = ""
#Client_ID = ""
#user_client = PyEng Bot 0.1
# details entered in praw.ini

subreddit = reddit.subreddit("pythonforengineers") #enter the targeted subreddit.

trigger_phase = "!bee"
lis = list()

with open('bee.txt', 'r') as f_in:
    lines = (line.rstrip() for line in f_in) 
    lines = list(line for line in lines if line) # Non-blank lines in a list
    lis = lines.copy()
    lis = list(filter(None, lis)	

#taking a line from the file by a randomly generated number using random module.

#checking every comment in the subreddit
for comment in subreddit.stream.comment():
    if trigger_phase in comment.body:
        reply_text = lines[random.randint(len(lis))]

        txt_fill = "The saying is:" + reply_text
        comment.reply(txt_fill)


