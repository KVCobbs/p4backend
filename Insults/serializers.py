from .models import Insult
from django.contrib.auth.models import User
from rest_framework import serializers


class InsultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email']
