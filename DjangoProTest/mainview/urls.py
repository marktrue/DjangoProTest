from django.conf.urls import patterns, include, url
from mainview import mainview

urlpatterns = patterns(
    '',
    url(r'^(?:index|index.html)?$', mainview.index),
    url(r'^list/(\d+)/$', mainview.list),
)