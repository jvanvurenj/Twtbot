from Models import User, Tweet
from peewee import *
import configparser

cfg_parser = configparser.ConfigParser()
database = cfg_parser['DEFAULT']['DATABASE']


class Database:
    def __init__(self):
        self.db = database
        self.db.connect()

    def add_user(self, user, followers_lst, following_lst):
        user = User.create(
            username = user,
            user_follows = following_lst,
            followers = followers_lst
        )

        return user     # A model instance
    
    def add_tweet(self, user, text):
        tweet = Tweet.create(
            username = user,     # NOTE: must be User instance
            content = text
        )

        return tweet

    def get_user(self, user):
        user = User.get(User.username == user)

        return user

    def get_tweet(self, user):
        pass

    def close(self):
        self.db.close()