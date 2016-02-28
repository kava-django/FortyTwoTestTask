from django.conf.urls import url
from .views import requests


urlpatterns = [
    url(r'^$', requests, name='requests'),

]
