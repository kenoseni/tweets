"""Functions run by background tasks to populate tweets"""

import os
import tweepy as tw
from django.db.models import Max
from itertools import islice
from datetime import datetime
from getTweeterTips.settings import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET)
from .models import Tip

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

def get_tweets(username):
    """Function that gets all tweets of a particular username

    Args: 
        username(str): username of tweets

    Returns:
        tweets(list): list of tweets for a particular username 
    """
    try:
        tweets = tw.Cursor(
            api.user_timeline,
            screen_name=username).items()
    except(Exception):
        return Exception
    return tweets

def tweet_generator(tweets):
    """Function creates the generator of the Tip model instance

    Args: 
        tweets(list): list of tweets for a particular username

    Yields:
        Tip(generator): generator of Tip instance
    """
    # get the most recent date from the database
    recent_tweet_at = Tip.objects.aggregate(recent_tweet_date=Max('tweeted_at'))
    
    for tweet in tweets:
        # line 52 to 62 will run when populating the database for the first time with tweets
        # line 63 to 73 will run when the database is updated with new tweets
        # the conditional statement on line 63 prevents duplication of already existing tweets in the database
        if 'RT @' not in tweet.text and not recent_tweet_at['recent_tweet_date'] :
            yield Tip(
                python_tip=tweet._json['text'],
                tweeted_at = datetime.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S %z %Y'),
                link = '' if not len(tweet._json[
                    'entities']['urls']) else tweet._json['entities']['urls'][0]['expanded_url'],
                who_posted=f"@{tweet._json['user']['screen_name']}",
                likes=tweet._json['favorite_count'],
                retweets=tweet._json.get('retweet_count', ''),
                published = False
                )
        elif 'RT @' not in tweet.text and datetime.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S %z %Y') > recent_tweet_at['recent_tweet_date']:
            yield Tip(
                python_tip=tweet._json['text'],
                tweeted_at = datetime.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S %z %Y'),
                link = '' if not len(tweet._json[
                    'entities']['urls']) else tweet._json['entities']['urls'][0]['expanded_url'],
                who_posted=f"@{tweet._json['user']['screen_name']}",
                likes=tweet._json['favorite_count'],
                retweets=tweet._json.get('retweet_count', ''),
                published = False
                )

def save_tweets_to_db(model, generator, batch_size=400):
    """Function that saves the python tips tweet into the database

    Args:
        model(object): class model for the tweets
        generator(generator): generator of model instance

    Returns:
        None 
    """
    tweets = []
    while True:
        # slice through the generator using the batch size as limit
        tweets.extend(list(islice(generator, batch_size)))
        if not list(islice(generator, batch_size)):
            break

    # bulk create tweet
    model.objects.bulk_create(tweets) 
