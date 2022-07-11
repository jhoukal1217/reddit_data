import os
import sys
from io import StringIO
from datetime import date, datetime, timedelta

import config as cfg
import praw
import boto3
from loguru import logger
from pandas import DataFrame

# logging
level = os.environ.get("LOGURU_LEVEL", "DEBUG")
logger.remove()
logger.add(sys.stdout, level=level)

# date vars
yesterday = date.today() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')

# file vars
file_name = ''.join([cfg.rdt_subreddit, '_', yesterday_str, '.csv'])


def connect_to_api():
    """connect to reddit api via praw library; returns connection instance
    """
    try:
        rdt_instance = praw.Reddit(client_id=cfg.rdt_client_id,
                                   client_secret=cfg.rdt_client_secret,
                                   user_agent=cfg.rdt_user_agent,
                                   username=cfg.rdt_username,
                                   password=cfg.rdt_password)
        return rdt_instance
    except Exception as e:
        logger.exception(f'issue with API: {e}')


def gather_posts(reddit):
    """query posts from designated subreddit; returns posts object
    """
    try:
        subreddit = reddit.subreddit(cfg.rdt_subreddit)
        posts = subreddit.top(time_filter=cfg.rdt_interval, limit=cfg.rdt_limit)
        return posts
    except Exception as e:
        logger.exception(f'issue gathering posts: {e}')


def extract_data(posts):
    """transforms list of dictionaries created from config-specified fields into dataframe
    """
    list_of_items = []
    df = None
    try:
        for post in posts:
            to_dict = vars(post)
            sub_dict = {field: to_dict[field] for field in cfg.post_fields}
            list_of_items.append(sub_dict)
            df = DataFrame(list_of_items)
            df['load_time'] = datetime.now()
    except Exception as e:
        logger.exception(f'issue extracting data: {e}')
    return df


def load_to_s3(data: DataFrame):
    """loads dataframe to s3 bucket
    """
    try:
        csv_buffer = StringIO()
        data.to_csv(csv_buffer)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(cfg.aws_s3_bucket, file_name).put(Body=csv_buffer.getvalue())
    except Exception as e:
        logger.exception(f'issue loading to s3: {e}')


def main():
    reddit = connect_to_api()
    posts = gather_posts(reddit)
    data = extract_data(posts)
    load_to_s3(data)


def lambda_handler(event, context):
    """Triggered from EventBridge.
    Args:
         event (dict): Event payload.
         context: Metadata for the event.
    """
    main()
