from django.contrib import admin
from user.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # 列表页面展示的数据
    list_display = ('username', 'email', 'source_type', 'user_type', 'date_joined')
    # 用作搜索的字段
    search_fields = ('user_type', 'username')

    # 对结果进行过滤
    list_filter = ('username',)

    # 可能回遇到mysql时区的问题，需要手动导入时区表
    # mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root -p mysql
    date_hierarchy = 'date_joined'

    # 指定排序，效果等同于Meta属性中的ordering
    ordering = ('date_joined', )

    # 详情页面展示的字段
    fields = ('username', 'date_joined', 'email', 'source_type', 'user_type')


admin.site.register(User, UserAdmin)