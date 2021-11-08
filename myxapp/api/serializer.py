from rest_framework import serializers
from rest_framework_mongoengine import serializers
from . models import User

class UserSerializer(serializers.DocumentSerializer):
    """ Serializing our User Object Document-> Import this to the view.py of our app for usage """
    class Meta:
        model = User
        fields = ('fname', 'lname','email','password')

