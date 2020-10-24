from django.contrib import admin
from user.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'source_type', 'user_type')


admin.site.register(User, UserAdmin)