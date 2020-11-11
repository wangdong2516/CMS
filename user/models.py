from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.model import BaseModel
# Create your models here.
# 根据已经存在的数据库生成模型类:使用`python manage.py inspectdb`命令就可以看到输出
# 生成的模型类不附加id字段，最好手动添加id字段，方便阅读和维护，manage=False表示Django不会管理这些表的生命周期
# https://docs.djangoproject.com/zh-hans/3.1/ref/models/options/#managed


class User(BaseModel, AbstractUser):
    """
        继承AbstractUser默认提供的字段
        不想要的可以直接置空
    """

    class UserTypeChoices(models.Choices):
        # 普通用户
        BASE = 1
        # VIP用户
        VIP = 2

    SOURCE_TYPE = [
        (1, 'qq'),
        (2, 'weixin'),
        (3, 'cms'),
        (4, 'other')
    ]
    source_type = models.IntegerField('用户来源', choices=SOURCE_TYPE, default=4)
    user_type = models.IntegerField('用户类型', choices=UserTypeChoices.choices, default=1)

    class Meta:
        db_table = 'user'
        ordering = ('-id', )

    def __str__(self):
        return self.username