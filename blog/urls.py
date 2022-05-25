from django.urls import re_path, include
from blog.views import *
app_name = 'blog'
urlpatterns = [
    re_path(r'^$', PostLV.as_view(), name='index'),  # /
    re_path(r'^post/$', PostLV.as_view(), name='post_list'),  # /post/
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),  # /post/slug 문구/
    re_path(r'^archive/$', PostAV.as_view(), name='post_archive'),  # /post/archive/
    re_path(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),  # /post/2012/
    re_path(r'^(?P<year>\d{4})/(?P<month>d{2})/$', PostMAV.as_view(), name='post_month_archive'),  # /post/2012/mon/
    re_path(r'^(?P<year>\d{4})/(?P<month>d{2})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),  # /post/2012/mon/12/
    re_path(r'today/$', PostTAV.as_view(), name='post_today_archive'),  # /post/today/
]
