from django.conf.urls import patterns, include, url
from adminxxzx import adminview

urlpatterns = patterns(
    '',
    url(r'^(?:index|index.html)?$', adminview.index),
    url(r'^logon$', adminview.logon),
    url(r'', adminview.notfound),
)