# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-06 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=50, verbose_name='课程标签'),
        ),
    ]
