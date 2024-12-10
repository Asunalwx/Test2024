
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='一个科室名称的名字应该唯一', max_length=128, unique=True, verbose_name='科室名称')),
                ('doctor_name', models.CharField(default='', max_length=128, verbose_name='医生名字')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '科室',
                'verbose_name_plural': '科室管理',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='医生的名字', max_length=128, verbose_name='姓名')),
                ('gender', models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='性别')),
                ('stu_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='工号')),
                ('idCard', models.CharField(blank=True, help_text='18位的身份证号码', max_length=18, null=True, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('enable', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.department', verbose_name='科室')),
            ],
            options={
                'verbose_name': '医生',
                'verbose_name_plural': '医生管理',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='一个病房的楼栋的名字应该唯一', max_length=128, unique=True, verbose_name='楼栋')),
                ('no', models.CharField(db_index=True, help_text='一个病房的房号应该唯一', max_length=128, unique=True, verbose_name='房号')),
                ('level', models.CharField(db_index=True, help_text='一个病房的床位的名字应该唯一', max_length=128, unique=True, verbose_name='床位')),
                ('amount', models.CharField(db_index=True, default='', max_length=128, verbose_name='人数')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '病房',
                'verbose_name_plural': '病房管理',
            },
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='名称')),
                ('prescription', models.IntegerField(choices=[(1, '是'), (2, '否')], default=2, verbose_name='是否处方药')),
                ('price', models.FloatField(verbose_name='价格')),
                ('qr_code', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='数量')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '药品',
                'verbose_name_plural': '药品管理',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='患者的名字', max_length=128, verbose_name='姓名')),
                ('gender', models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='性别')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('in_time', models.DateTimeField(verbose_name='就诊时间')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.department', verbose_name='就诊科室')),
                ('doctor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.doctor', verbose_name='就诊医生')),
                ('idCard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.house', verbose_name='房号')),
            ],
            options={
                'verbose_name': '患者',
                'verbose_name_plural': '患者管理',
            },
        ),
    ]
