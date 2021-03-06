# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-17 06:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_detailinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankNo', models.CharField(max_length=50, verbose_name='卡号')),
                ('bank', models.IntegerField(choices=[('0', '未绑定'), ('1', 'CBC'), ('2', 'ABC'), ('3', 'BC'), ('4', 'ICBC')], default=0, verbose_name='银行')),
                ('bankpwd', models.CharField(max_length=200, verbose_name='交易密码')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '银行信息',
                'verbose_name': '银行信息列表',
            },
        ),
    ]
