#https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
#to run this enter this at command line:
#python helloworld.py helloworld.txt


#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#time will allow us to schedule intervals between our Tweets (so we don’t get in trouble with Twitter), 
#sys will allow us to feed our robot a file for it to read and Tweet.
import tweepy, time, sys

#We’re assigning our text file to argfile
#What we are saying here is that argfile contains the string, helloworld.txt
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'XXX'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'XXX'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'XXX'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'XXX'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
#open, read, close the helloworld.txt file
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
 
#Using a for loop, we iterate through every line stored in f. 
#For each line, we send out a Tweet using api.update_status(line). Then we tell our robot to snooze with time.sleep(900). 
#The for loop will continue until it reads and Tweets the last line in f(or finds an error in your file), and will then exit.
 
for line in f:
    api.update_status(line)
    time.sleep(30)#Tweet every 30 seconds