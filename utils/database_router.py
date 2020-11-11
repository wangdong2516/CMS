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
        """指定用于读取的数据库,没有建议，返回None"""
        if model._meta.app_label == 'user':
            return 'default'
        return 'other'

    def db_for_write(self, model, **hints):
        """指定用于写入的数据库，没有建议，返回None"""
        if model._meta.app_label == 'user':
            return 'default'
        return 'other'

    def allow_relation(self, obj1, obj2, **hints):
        """
            确定obj1和obj2之间是否可以产生关联， 主要用于foreign key和 many to many操作
            如果允许obj1和obj2之间的关系，返回True，如果阻止关系，返回False，没有意见，返回None
        """
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
            是否允许迁移操作在别名为db的数据库中运行，允许返回True，否则返回False,没有意见返回None
        :param db: 迁移的数据库
        :param app_label: 应用程序的标签
        :param model_name: 模型类的名称
        :param hints: 附加信息
        :return:
        """
        return None