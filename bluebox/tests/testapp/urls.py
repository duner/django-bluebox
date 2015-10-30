from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
	url(r'^test-middleware-view/$', TestMiddlewareView.as_view(), name='test-middleware'),
)
