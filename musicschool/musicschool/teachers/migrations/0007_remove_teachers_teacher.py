# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_auto_20180525_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='teacher',
        ),
    ]
