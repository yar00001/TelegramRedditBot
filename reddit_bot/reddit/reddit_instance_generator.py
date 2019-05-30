import configparser
import praw
import os

class RedditInstance:
    configFilePath = 'config/reddit.properties'
    reddit_config = configparser.ConfigParser()
    reddit_config.read(configFilePath)

    # Application Related Configs
    app_name = reddit_config.get('APP', 'AppName')
    app_client_id = reddit_config.get('APP', 'AppClientId')
    app_client_secret = reddit_config.get('APP', 'AppClientSecret')
    app_user_agent = reddit_config.get('APP', 'AppUserAgent')

    # User Related Configs
    user_username = reddit_config.get('USER', 'UserName')
    user_password = reddit_config.get('USER', 'Password')

    # Make the call - Only for Script type app
    reddit = praw.Reddit(client_id=app_client_id,
                         client_secret=app_client_secret,
                         password=user_password,
                         user_agent=app_user_agent,
                         username=user_username)

    reddit_read_only = praw.Reddit(client_id=app_client_id,
                                   client_secret=app_client_secret,
                                   user_agent=app_user_agent)

    def get_read_only_instance(self):
        return self.reddit_read_only
