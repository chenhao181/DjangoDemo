from django.contrib import admin
from .models import BookInfo, PeopleInfo
# Register your models here.

# 注册模型类
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# 重新运行django

