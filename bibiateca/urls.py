from django.conf.urls import patterns, include, url
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

from bibiateca.library import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
