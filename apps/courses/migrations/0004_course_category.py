# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-06 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='后端开发', max_length=300, verbose_name='课程类别'),
        ),
    ]
