# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymtracker', '0003_remove_userperformed_performedwithdumbbells'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperformed',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
