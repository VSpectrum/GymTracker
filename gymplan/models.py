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
    sets = models.SmallIntegerField()

    class Meta:
        verbose_name = 'User\'s Exercise Reps'
        verbose_name_plural = 'User\'s Exercises Reps'

    def __unicode__(self):
        return str(self.sets)


class UserExerciseTemplate(models.Model):
    user = models.ForeignKey(User)
    isFixedReps = models.BooleanField(default=True)  # if this is false then it implies Weight is fixed but reps change

    class Meta:
        verbose_name = 'User\'s Template'
        verbose_name_plural = 'User\'s Templates'

    def __unicode__(self):
        return str(self.reps)


class FrequencyHandler(models.Model):  # how to handle which exercises are assigned to what day/session
    pass