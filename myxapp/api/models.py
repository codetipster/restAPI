# from django.db import models
from mongoengine import *
import datetime

from mongoengine.document import Document, EmbeddedDocument, EmbeddedDocumentList
from mongoengine.fields import EmailField, StringField, DateTimeField, BooleanField, ListField, ReferenceField
# Create your models here.

class User(Document):
    """ A User document that defines fields for our app users """

    fname = StringField(max_length=50, required=True)
    lname = StringField(max_length=50, required=True)
    email = EmailField(max_length=255, unique=True)
    password = StringField(max_length=100, required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    is_active = BooleanField(default=True)

# class UserInterests(EmbeddedDocument):
#     pass

# class UserExpertAreas(EmbeddedDocument):
#     pass

# class UserInfo(EmbeddedDocument):
#     pass


# class Profile(Document): #Upon authentication, users should be able to create profile
#     """Every User sets their profile with this model"""

#     user = ReferenceField(User) #Every user has a profile
#     interested_in = ListField(EmbeddedDocumentList(UserInterests))
#     expert_in = ListField(EmbeddedDocumentList(UserExpertAreas))
#     basic_info = ListField(EmbeddedDocumentList(UserInfo))