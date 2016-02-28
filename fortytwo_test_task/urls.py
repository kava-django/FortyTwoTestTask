from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^requests/', include('apps.requests.urls')),
    url(r'^$', include('apps.hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
