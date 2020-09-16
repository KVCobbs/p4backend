from django.contrib import admin
from django.urls import path
from rest_framework import routers
from insults.views import InsultViewSet
from profiles import views
from profiles.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'Profile',views.ProfileViewset)

