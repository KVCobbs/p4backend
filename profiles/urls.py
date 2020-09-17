from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from authentication.models import User
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')

custom_urlpatterns = [
    url(r'users/(?P<user_pk>\d+)/$', ProfileViewSet.as_view({'get': 'list'}))
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
