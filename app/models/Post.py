from mongoengine import *
import datetime

class Post(Document):
	title = StringField(max_length=200, required=True)
	text = StringField(max_length=200, required=True)
	author = StringField(max_length=200, required=True)
	upvotes = IntField(min_value=0)