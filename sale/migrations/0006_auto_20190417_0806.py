# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-17 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_auto_20190417_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='examine',
            field=models.IntegerField(choices=[(0, '审核中'), (1, '审核通过'), (2, '审核未通过')], default=0, verbose_name='审核进度'),
        ),
    ]