import tweepy
import time
consumer_key='3VmSuIqYQJidDJbF2UuJ7nWti'
consumer_secret='N53DOQgwaOs4Qq1qJLToYyQlOTy5xJZ2BI2cq2tHhHH0eoErNl'
key='1596936405284188161-I6q2qEW6wSfIKJn6LmaEPL0nwAZbhg'
secret='x1wVu7wtt2egQA6b7XW2TRVMy9gYvOaoFiFjFx4zF2cDo'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)
api=tweepy.API(auth)
hashtag="javascript"
tweetNumber=3
tweets=tweepy.Cursor(api.search,hashtag).items(tweetNumber)
def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchbot()