from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^myadmin/', include('myadmin.urls')),
    url(r'^', include('myweb.urls')),
]
