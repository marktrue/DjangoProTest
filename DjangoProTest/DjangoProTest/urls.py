from django.conf.urls import patterns, include, url
import mainview.urls
import adminxxzx.urls
from DjangoProTest import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'DjangoProTest.views.home', name='home'),
    # url(r'^DjangoProTest/', include('DjangoProTest.DjangoProTest.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^djgadmin/?', include(admin.site.urls)),
    url(r'^adminxxzx/?', include(adminxxzx.urls)),
    url(r'^', include(mainview.urls)),
)
