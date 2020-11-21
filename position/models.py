from django.db import models

# Create your models here.


class PositionModel(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='职位名称')
    job_type = models.CharField(max_length=20, verbose_name='职位类型')
    url = models.URLField(max_length=50, verbose_name='链接')
    source = models.CharField(max_length=25, verbose_name='来源')
    work_experience = models.CharField(max_length=30, verbose_name='工作经验')
    degree = models.CharField(max_length=20, verbose_name='学历')
    salary = models.CharField(max_length=10, verbose_name='薪资')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_valid = models.BooleanField(default=True, verbose_name='是否有效')

    class Meta:
        db_table = 'position'
        managed = False
        verbose_name = '职位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name