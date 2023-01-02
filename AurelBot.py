import tweepy
import time
f = open('quotes.txt', encoding="utf8")


auth = tweepy.OAuthHandler("KmvzH8BgOgFhbuqWkYMC49cOi", "24R7sZGPtsZrkhjov3WrsfZPXLvnM45fA4bfgMgy4QVCaPrdj7")
auth.set_access_token("1608864958787293185-KtLrcWIMvPhsEpskHnLHJyOKDsdIQE", "UhTQiRIbsP749C05gOjJZoIk98YSC4lWeF2UWvCzpUFNL")

bot = tweepy.API(auth)

for line in f.readlines():
    bot.update_status(f"{line} -Marcus Aurelius")
    time.sleep(28800)
    