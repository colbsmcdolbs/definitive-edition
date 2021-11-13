from mongoengine import *
from enums import Genre
from models import Port


class Game(Document):
    title = StringField(required=True, max_length=128)
    image_url = StringField()
    genres = ListField(EnumField(Genre))
    ports = ListField(EmbeddedDocumentField(Port))
