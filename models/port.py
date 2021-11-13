from mongoengine import *
from enums import Platform


class Port(EmbeddedDocument):
    release_date = DateField(required=True)
    alternate_title = StringField()
    console = EnumField(Platform)
