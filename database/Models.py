from peewee import *
from Fields import ListField
import configparser

cfg_parser = configparser.ConfigParser()
db = cfg_parser['DEFAULT']['DATABASE']


class BaseModel(Model):
    '''
    Implements inner Meta class, used in all subclasses to determine database
    '''
    class Meta:
        database = db


class User(BaseModel):
    '''
    Implements the User table.

    username: Username of user
    user_follows: Users that this user follows
    followers: Users that follow this user
    '''

    username = CharField()
    user_follows = ListField()
    followers = ListField()


class Tweet(BaseModel):
    '''
    Implements the Tweet table.

    username: Username of the user who posted the Tweet
    content: Text content found within the Tweet
    '''
    
    username = ForeignKeyField(User, backref='tweets')
    content = TextField()
