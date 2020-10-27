"""
    自定义数据库的路由:
        1. 需要给作出选择的数据库指定app_label
        2. 定义Database Routers确定哪个模型使用哪个数据库
        3. 在配置文件中指定DATABASES_APPS_MAPPING和DATABASE_ROUTERS
"""

from django.conf import settings

DATABASE_MAPPING = settings.DATABASES_APPS_MAPPING  # 在setting中定义的路由表


class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        """指定用于读取的数据库"""
        if model._meta.app_label == 'user':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """指定用于写入的数据库"""
        if model._meta.app_label == 'user':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """确定obj1和obj2之间是否可以产生关联， 主要用于foreign key和 many to many操作"""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None
