from peewee import *
from Models import User, Tweet
import configparser

cfg_parser = configparser.ConfigParser()
db = cfg_parser['DEFAULT']['DATABASE']


def create_tables():
    with db:
        db.create_tables([User, Tweet])

create_tables()