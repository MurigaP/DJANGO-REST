__author__ = 'hudutech'
from django.conf.urls import url
from api.v1 import api_controller as views

urlpatterns = [
    url('^consumers/$',views.consumer_endpoint, name='consumer_endpoint'),
]