# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as datetime
from django.contrib.auth.models import User
# Create your models here.

from gymplan.models import *


class UserPerformed(models.Model):
    exercise = models.ForeignKey(UserExercises)
    set_number = models.SmallIntegerField()
    variableIsReps = models.BooleanField(default=False)
    numberPerformed = models.SmallIntegerField()  # number being either reps or weight depending on variableIsReps
    date = models.DateTimeField(default=datetime.now, blank=False)

    class Meta:
        verbose_name = 'User\'s Reps Data'
        verbose_name_plural = 'User\'s Reps Data'

    def __unicode__(self):
        return str(self.numberPerformed)
