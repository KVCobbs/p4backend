from .models import Insult
from django.contrib.auth.models import User
from rest_framework import serializers


class InsultSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Insult
        fields = ['user', 'text']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email']
