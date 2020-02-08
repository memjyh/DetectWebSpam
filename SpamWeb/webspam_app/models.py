from django.db import models
import mongoengine

mongoengine.connect('test',host='127.0.0.1')

class WebSpamModel(mongoengine.Document):
    url=mongoengine.StringField()
    host=mongoengine.StringField()
    html_content=mongoengine.StringField()

    meta={'collection':'runoob'}

# Create your models here.
