#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random, json, re, datetime

random.seed()
def parseIn():
    i = 0
    blackcards = []
    f = open('blackcards.txt', 'r')
    line = f.readline() #Read a line from the file
    while (line != ''):
	       line = re.sub('\s+',' ',line)
	       blackcards.append(line)             #Store the word
	       i = i + 1
	       line = f.readline() #Read a new line


    i = 0
    whitecards = []
    f = open('whitecards.txt', 'r')
    line = f.readline() #Read a line from the file
    while (line != ''):
	       line = re.sub('\s+',' ',line)
	       whitecards.append(line)             #Store the word
	       i = i + 1
	       line = f.readline() #Read a new line

    return blackcards, whitecards

#end parseIn

def newtweet():
    blackcards, whitecards = parseIn()
    blackcardsN = random.randint(0, blackcards.__len__())
    whitecardsN = random.randint(0, whitecards.__len__())
    tweet = blackcards[blackcardsN]
    tweet = tweet.replace('__________', " " + whitecards[whitecardsN] + " ")

    tweet = re.sub('\s+',' ',tweet) #Removes all whitespaces and replaces them with spaces

    return tweet





#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while(True):
	text=newtweet(1)
	if(len(text)<140):
		print "Generating...\n"
		text=newtweet()
		print text
        print "\nTweeting..."
		api.update_status(status=text)
		print "Tweeted!"
		time.sleep(1800)#Tweet every 30 minutes
