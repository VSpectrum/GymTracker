# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20170815_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisemusclegroups',
            name='exerciseName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.ExerciseName'),
        ),
    ]
