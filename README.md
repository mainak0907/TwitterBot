# Twitter Bot for Hashtag Interaction
A Twitter bot, designed to monitor mentions containing specific hashtags, reply to those tweets, favorite them, and retweet them. The bot is built using the Tweepy library and utilizes Twitter's API.

Built Using -
1. Twitter API and OAuth Handler
2. Tweepy Module of Python
3. Bash Cloud (PythonAnywhere), can run continuously for 24 hours

If you are on Twitter then You can try it out.
Don't forget to mention @RooeBot and use hashtags like #codedays #day #consistency
It can be used for maintaining consistency in learning where people can share their learning journey every day and the bot will promote it and can also be used for HashTag marketing.

With further modifications,( Using sentiment analysis, and DM features) this can be turned into a bot that can automate Twitter customer management for Commercial Companies.


## Features

- Monitors Twitter mentions in real-time.
- Replies to tweets containing the hashtags `#codedays` or `#day`.
- Favorites and retweets the mentioned tweets.
- Keeps track of the last seen tweet ID to avoid duplicate interactions.

## Prerequisites

- Python 3.x
- Tweepy library (install using `pip install tweepy`)

## Getting Started

1. Clone this repository to your local machine.
2. Create a Twitter Developer account and set up a new Twitter App to obtain the necessary API keys and tokens.
3. Replace the placeholder values in the script with your actual API keys and tokens.
4. Customize the reply message as needed.
5. Run the script using the command `python twitter_bot.py`.

## Configuration

In the `twitter_bot.py` script, make sure to update the following variables with your actual Twitter API credentials:

```python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
key = 'YOUR_ACCESS_TOKEN_KEY'
secret = 'YOUR_ACCESS_TOKEN_SECRET'
