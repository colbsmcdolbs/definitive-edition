from mongoengine import *
import datetime


class User(Document):
    email = StringField(max_length=128, required=True)
    password_hash = StringField(required=True)
    user_name = StringField(required=True, max_length=32)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
