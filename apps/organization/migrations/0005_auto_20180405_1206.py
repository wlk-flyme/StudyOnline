# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-05 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180404_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='work_years',
            field=models.CharField(default=0, max_length=20, verbose_name='工作年限'),
        ),
    ]
