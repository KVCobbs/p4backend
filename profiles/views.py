import profile

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Profile
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework import permissions
from .serializers import ProfileSerializer


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProfileSerializer

    # Select all
    def get_queryset(self):
        queryset = Profile.objects.all().filter(user=self.request.user)
        return queryset

    # Create
    def create(self, request, *args, **kwargs):
        insult = Profile.objects.filter(
            user=request.data.get('user'),
        )

        if profile:
            msg = "You cannot change your profile picture right now"
            raise ValidationError(msg)
        return super().create(request)

    def preform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, profile="", *args, **kwargs):
        profile = profile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.user:
            raise PermissionDenied("Lol Loser. You cannot delete this")
        return Response({super().destroy(request, *args, **kwargs), })
