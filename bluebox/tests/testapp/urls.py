from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns(
    url(r'^object/(?P<id>[-\w]+)/$', MockDetailView.as_view(), name='mock-detail'),
)