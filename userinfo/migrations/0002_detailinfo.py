# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-17 06:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('ads', models.TextField(verbose_name='住址')),
                ('identity', models.CharField(max_length=18, verbose_name='身份证号')),
                ('sex', models.IntegerField(choices=[('0', '男'), ('1', '女')], default=0, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('cellphone', models.CharField(max_length=20, verbose_name='电话')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户信息列表',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
