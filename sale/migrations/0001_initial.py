# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-17 07:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_brand', models.ImageField(default='normal,png', upload_to='static/image', verbose_name='标志')),
                ('btitle', models.CharField(max_length=50, verbose_name='名称')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '汽车品牌列表',
                'verbose_name_plural': '汽车品牌',
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=50, verbose_name='车名')),
                ('regist_date', models.DateField(verbose_name='上牌日期')),
                ('engineNo', models.CharField(max_length=50, verbose_name='发动机号')),
                ('mileage', models.ImageField(upload_to='', verbose_name='公里数')),
                ('maintenance', models.BooleanField(default=False, verbose_name='维修记录')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('extractprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('newprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('picture', models.ImageField(default='normal.png', upload_to='static/image', verbose_name='图片')),
                ('formalities', models.BooleanField(default=True, verbose_name='手续')),
                ('debt', models.BooleanField(default=False, verbose_name='债务')),
                ('promise', models.TextField(verbose_name='承诺')),
                ('examine', models.IntegerField(choices=[('0', '审核中'), ('1', '审核通过'), ('2', '审核未通过')], default=0, verbose_name='审核进度')),
                ('isPurchase', models.BooleanField(default=False, verbose_name='是否购买')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Brand', verbose_name='品牌')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '汽车信息列表',
                'verbose_name_plural': '汽车信息',
            },
        ),
    ]