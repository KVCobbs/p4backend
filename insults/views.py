from django.shortcuts import render
from .models import Insult
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InsultSerializer, UserSerializer,

# Create your views here.
