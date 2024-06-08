from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)



class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题', max_length=32)


class Employee(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    age = models.IntegerField()
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')
    depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)