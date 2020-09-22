from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from profiles.models import Profile
from .models import Insult
# from django.contrib.auth.models import User
from authentication.models import User
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework import permissions
from .serializers import InsultSerializer, UserSerializer


# Create your views here.

# old
class InsultViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = InsultSerializer

    # Select all
    def get_queryset(self):
        queryset = Insult.objects.all().filter(user=self.request.user)
        return queryset

    # Create
    def create(self, request, *args, **kwargs):
        print(request.user)
        insult = Insult.objects.filter(
            user=request.data.get('user'),
            text=request.data.get('text'),
        )

        if insult:
            msg = "This insult isn't very creative"
            raise ValidationError(msg)
        return super().create(request)

    def preform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        insult = Insult.objects.get(pk=self.kwargs["pk"])
        if not request.user == insult.user:
            raise PermissionDenied("Lol Loser. You cannot delete this")
        return Response({super().destroy(request, *args, **kwargs), })


# new
class UserInsultViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = InsultSerializer

    # Select all
    def get_queryset(self):
        queryset = Insult.objects.all().filter(user=User.objects.get(pk=self.kwargs["user_pk"]))
        return queryset

    # Create
    def create(self, request, *args, **kwargs):
        print(request.user)
        insult = Insult.objects.filter(
            user=request.data.get('user'),
            text=request.data.get('text'),
        )

        if insult:
            msg = "This insult isn't very creative"
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        insult = Insult.objects.get(pk=self.kwargs["pk"])
        if not request.user == insult.user:
            raise PermissionDenied("Lol Loser. You cannot delete this")
        return Response({super().destroy(request, *args, **kwargs), })
