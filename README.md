# twitter_bot

## Building a twitter bot

- [here is a tutorial I liked](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)
- What this bot does: tweets out lines from a given text file every few minutes.  It goes until it hits the end of the text file.
- [here's the bot I made](https://twitter.com/harric17)  (I later reused this Twitter account for an department event)
- For those unfamiliar with [the Vengaboys](https://www.youtube.com/embed/6Zbi0XmGtMw)


## How this twitter bot works

<img src="https://a.slack-edge.com/ae7f/img/services/twitter_512.png" height="200" width="200" align="right">

- First you need to set up a secure way of interacting with twitter via
[twitter's website for developers](https://dev.twitter.com/apps/new)
    - Enter the following in both code and twitter site for [secure communication](https://stackoverflow.com/questions/28057430/what-is-the-access-token-vs-access-token-secret-and-consumer-key-vs-consumer-s):
        - client key/secret: identifies the service (here twitter) to your machine
        - access key/secret: defines access privledges for the service on your machine, e.g. what data can/cant be accessed.  Service sends this to your machine to perform any action.
- The Python code is very minimal
    - 1 line of code so user can specify text file at command prompt, ie >>python twitterbot.py stufftotweet.txt
    - read in text file
    - for loop iterates over each line of text file
    - [tweepy library](http://www.tweepy.org) makes the twitter actions simple
          - tons of out of the box methods for all types of twitter stuff: tweeting, favoriting, blocking, direct messaging, etc.
