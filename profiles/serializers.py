from .models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = [""]
