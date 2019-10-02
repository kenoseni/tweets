import os
from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from .models import Tip
from .python_tips import get_tweets, save_tweets_to_db, tweet_generator

# task logger
logger = get_task_logger(__name__)
name =  os.getenv('TWEET_NAME', '')

# This task is set to run every 5 minutes
@periodic_task(
    run_every=(crontab(minute='*/5')),
    name=name)
def get_tweet():
    """Function that runs periodically to get tweets and save
    in database
    """
    logger.info('----------Getting tweets--------')
    tweets = get_tweets('python_tip')
    save_tweets_to_db(Tip, tweet_generator(tweets))
    logger.info('----------Done, tweets saved in database---------')
