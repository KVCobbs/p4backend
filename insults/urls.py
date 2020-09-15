from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from insults.models import Insult
from insults.views import InsultViewSet

router = routers.DefaultRouter()
router.register('insults', InsultViewSet, basename='insults')

custom_urlpatters = [
    url(r'insults/(?P<insults_pk>\d+)/$', Insult.as_view(), name='Insults'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatters
