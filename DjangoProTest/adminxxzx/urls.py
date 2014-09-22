from django.conf.urls import patterns, include, url
from adminxxzx import adminview
from adminxxzx.views import AdminxxzxView

urlpatterns = patterns(
    '',
    url(r'^(?:index|index.html)?$', adminview.index),
    url(r'^logon$', adminview.logon),
    url(r'^test$', AdminxxzxView.as_view()),
    url(r'^newArticle.html$',adminview.addArticle),
    url(r'^getmenu$',),
    url(r'', adminview.notfound),
)