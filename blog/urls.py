from django.urls import path, include
from blog.views import *

urlpatterns = [
    path(r'^$', PostLV.as_view(), name='index'),  # /
    path(r'^post/$', PostLV.as_view(), name='post_list'),  # /post/
    path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),  # /post/slug 문구/
    path(r'^archive/$', PostLV.as_view(), name='post_archive'),  # /post/archive/
    path(r'^(?P<yaer>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),  # /post/2012/
    path(r'^(?P<yaer>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),  # /post/2012/mon/
    path(r'^(?<yaer>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),  # /post/2012/mon/12/
    path(r'^today/$', PostTAV.as_view(), name='post_today_archive')  # /post/today/
]
