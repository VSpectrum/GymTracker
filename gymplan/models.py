# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from exercises.models import ExerciseName


class UserExercises(models.Model):
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(ExerciseName, blank=False)

    class Meta:
        verbose_name = 'User\'s Exercise'
        verbose_name_plural = 'User\'s Exercises'

    def __unicode__(self):
        return self.exercise


class UserExercisesSetReps(models.Model):
    userExercise = models.ForeignKey(UserExercises)
    reps = models.SmallIntegerField(blank=False)

    class Meta:
        verbose_name = 'User\'s Exercise Reps'
        verbose_name_plural = 'User\'s Exercises Reps'

    def __unicode__(self):
        return str(self.reps)
