# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymplan', '0006_auto_20170820_1650'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExerciseGroupSchedule',
            new_name='ExerciseSessionSchedule',
        ),
        migrations.AlterModelOptions(
            name='exercisesessionschedule',
            options={'verbose_name': "User's Exercise Session Schedule", 'verbose_name_plural': "User's Exercises Session Schedule"},
        ),
    ]
