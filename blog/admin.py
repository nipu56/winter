from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')  # 제목과 수정날짜 출력
    list_filter = ('modify_date',)  # 필터기준 = 수정날짜
    search_fields = ('title', 'content')  # 검색범위 = 제목, 내용
    prepopulated_fields = {'slug': ('title',)}  # slug 필드 제목으로 자동 채우기


admin.site.register(Post, PostAdmin)
