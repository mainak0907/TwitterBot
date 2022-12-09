import tweepy
import time
consumer_key='3VmSuIqJidDJbF2UuJ7nWti'
consumer_secret='N53DOQgwaOs4Qq1qToYyQlOTy5xJZ2BI2cq2tHhHH0eoErNl'
key='1596936405284188161-I6q2qEwSfIKJn6LmaEPL0nwAZbhg'
secret='x1wVu7wtt2egQA6b7X2TRVMy9gYvOaoFiFjFx4zF2cDo'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)
api=tweepy.API(auth)
#api.update_status("Hey from Twitter bot - First Tweet")
#print("Status Updated")
FILE_NAME='last_seen.txt'
def read_last_seen(FILE_NAME):
    file_read=open(FILE_NAME,'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id
def store_last_seen(FILE_NAME,last_seen_id):
    file_write=open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
def reply():
    tweets=api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
       if '#codedays' or '#day' in tweet.full_text.lower():
         print("New Tweet found")
         print("Replied to ID- "+str(tweet.id))
         api.update_status("@"+tweet.user.screen_name+" Good luck Mate!! Keep Up the consistency", tweet.id)
         api.create_favorite(tweet.id)
         api.retweet(tweet.id)
         store_last_seen(FILE_NAME,tweet.id)
while True:
 reply()
 time.sleep(30)
