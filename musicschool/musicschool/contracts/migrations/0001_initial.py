# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('lesson_type', models.CharField(max_length=200)),
                ('lesson_duration', models.DurationField()),
                ('lesson_cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]