# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MacroBody(models.Model):
    macroDesc = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        verbose_name = 'Macro Body Part'
        verbose_name_plural = 'Macro Body Parts'

    def __unicode__(self):
        return self.macroDesc

    def as_json(self):
        return dict(
            macroDesc=self.macroDesc
        )


class MicroBody(models.Model):
    macroBody = models.ForeignKey(MacroBody, blank=False)
    microDesc = models.CharField(max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = 'Micro Body Part'
        verbose_name_plural = 'Micro Body Parts'

    def __unicode__(self):
        return self.microDesc

    def as_json(self):
        return dict(
            macroBody=self.macroBody.macroDesc,
            microDesc=self.microDesc
        )


class ExerciseName(models.Model):
    exerciseName = models.CharField(max_length=50, unique=True)
    isApproved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Exercise/Movement'
        verbose_name_plural = 'Exercises/Movements'

    def __unicode__(self):
        return self.exerciseName

    def as_json(self):
        return dict(
            exerciseName=self.exerciseName
        )


class ExerciseMuscleGroups(models.Model):
    exerciseName = models.ForeignKey(ExerciseName, blank=False)
    targetMicro = models.ForeignKey(MicroBody, blank=True)
    targetMacro = models.ForeignKey(MacroBody, blank=False)

    class Meta:
        verbose_name = 'Exercise Target Muscle'
        verbose_name_plural = 'Exercise Target Muscles'

    def __unicode__(self):
        return self.exerciseName.exerciseName

    def as_json(self):
        return dict(
            exerciseName=self.exerciseName.exerciseName,
            targetMicro=self.targetMicro.microDesc,
            targetMacro=self.targetMacro.macroDesc
        )


class ExerciseTips(models.Model):
    exerciseName = models.ForeignKey(ExerciseName, blank=False)
    exerciseTip = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Exercise Tip'
        verbose_name_plural = 'Exercise Tips'

    def __unicode__(self):
        return self.exerciseName.exerciseName

    def as_json(self):
        return dict(
            exerciseName=self.exerciseName.exerciseName,
            exerciseTip=self.exerciseTip
        )
