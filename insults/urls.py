from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from authentication.models import User
from insults.models import Insult
from insults.views import InsultViewSet, UserInsultViewSet

router = routers.DefaultRouter()
router.register('insults', InsultViewSet, basename='insults')

custom_urlpatterns = [
    url(r'users/(?P<user_pk>\d+)/$', UserInsultViewSet.as_view({'get': 'list'}), name='user_insults'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
