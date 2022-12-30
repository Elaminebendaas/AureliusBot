import tweepy
import time

auth = tweepy.OAuthHandler("lXT8j2f1NCSu2P4fJMAC6gIw3", "eldIsvpYcv3KcvGf6vSbjhiJMmczuWAwq47UeZaDFSKq0Fpfjs")
auth.set_access_token("1608864958787293185-ri4QSX0fibyn3vsYTeLoKbsuDCijcq", "NT1DDeGEgNQyuGGz72mM3gW9RsQ4jtJFeMMT5S4ERlqNC")

bot = tweepy.API(auth)

https://realpython.com/twitter-bot-python-tweepy/
bot.update_status("Hello, this is a test!")
