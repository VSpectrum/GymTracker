# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MacroBody(models.Model):
    macroDesc = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = 'Macro Body Part'
        verbose_name_plural = 'Macro Body Parts'

    def __unicode__(self):
        return self.macroDesc


class MicroBody(models.Model):
    majorBody = models.ForeignKey(MacroBody)
    microDesc = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'Micro Body Part'
        verbose_name_plural = 'Micro Body Parts'

    def __unicode__(self):
        return self.microDesc


class ExerciseName(models.Model):
    exerciseName = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Exercise/Movement'
        verbose_name_plural = 'Exercises/Movements'

    def __unicode__(self):
        return self.exerciseName


class ExerciseMuscleGroups(models.Model):
    exerciseName = models.ForeignKey(ExerciseName)
    targetMicro = models.ForeignKey(MicroBody, blank=True)
    targetMacro = models.ForeignKey(MacroBody, blank=False)

    class Meta:
        verbose_name = 'Exercise Target Muscle'
        verbose_name_plural = 'Exercise Target Muscles'

    def __unicode__(self):
        return self.exerciseName
