from django.db import models

# Create your models here.

from django.urls import reverse
from django.utils import timezone



class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='科室名称', help_text='一个科室名称的名字应该唯一', unique=True, db_index=True)
    doctor_name = models.CharField(max_length=128, verbose_name='医生名字',default="")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "科室"
        verbose_name_plural = "科室管理"

    def __str__(self):
        return self.name






class Doctor(models.Model):
    name = models.CharField(max_length=128, verbose_name='姓名', help_text='医生的名字', null=False, blank=False,
                            db_index=True)
    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)
    stu_no = models.CharField(max_length=20, verbose_name="工号", null=True, blank=True,)
    idCard = models.CharField(max_length=18, verbose_name='身份证号', help_text='18位的身份证号码', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='科室',
                                   db_index=True)
    enable = models.BooleanField(verbose_name='状态', default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "医生"
        verbose_name_plural = "医生管理"

    def __str__(self):
        return self.name



class House(models.Model):
    name = models.CharField(max_length=128, verbose_name='楼栋', help_text='一个病房的楼栋的名字应该唯一', unique=True, db_index=True)
    no = models.CharField(max_length=128, verbose_name='房号', help_text='一个病房的房号应该唯一', unique=True, db_index=True)
    level = models.CharField(max_length=128, verbose_name='床位', help_text='一个病房的床位的名字应该唯一', unique=True, db_index=True)
    amount = models.CharField(max_length=128, verbose_name='人数', db_index=True,default="")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "病房"
        verbose_name_plural = "病房管理"

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=128, verbose_name='姓名', help_text='患者的名字', null=False, blank=False,
                            db_index=True)
    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)
    idCard = models.ForeignKey(House, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='房号',
                               db_index=True)
    phone = models.CharField(max_length=11, verbose_name='手机号')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='就诊科室',
                                   db_index=True)
    in_time = models.DateTimeField(verbose_name='就诊时间')
    doctor_name = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='就诊医生',
                                    db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    class Meta:
        verbose_name = "患者"
        verbose_name_plural = "患者管理"

    def __str__(self):
        return self.name







class Medical(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', unique=True, db_index=True)
    prescription_choices = (
        (1, '是'),
        (2, '否'),
    )
    prescription = models.IntegerField(choices=prescription_choices, verbose_name='是否处方药', default=2)
    price = models.FloatField(verbose_name='价格')
    qr_code = models.CharField(max_length=128, verbose_name='数量', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "药品"
        verbose_name_plural = "药品管理"