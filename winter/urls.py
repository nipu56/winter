from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path('admin/', admin.site.urls),# /admin/
    
    re_path(r'^$', HomeView.as_view(),name='home'),# /
    re_path(r'^blog/', include('blog.urls', ), name='blog'), # /blog/
    
]
