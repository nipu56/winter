from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include('blog.urls')),
    re_path('blog/', include('blog.urls', ), name='blog'),

]
