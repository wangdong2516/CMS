from django.contrib import admin
from position.models import PositionModel
# Register your models here.


class PositionAdminModel(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'is_valid', 'id')
    fields = ('name', 'id', 'is_valid')


admin.site.register(PositionModel, PositionAdminModel)