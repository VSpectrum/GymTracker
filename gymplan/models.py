# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from exercises.models import ExerciseName


class UserExercises(models.Model):
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(ExerciseName, blank=False)

    exercisedWith_choices = (
        ('M', "Machines"),
        ('D', "Dumbbells"),
        ('B', "Barbell"),
        ('C', "Cable")
    )

    performedWith = models.CharField(
        max_length=1,
        choices=exercisedWith_choices,
        default="D",
    )

    class Meta:
        verbose_name = 'User\'s Exercise'
        verbose_name_plural = 'User\'s Exercises'

    def __unicode__(self):
        return self.exercise.exerciseName


class UserExercisesSetReps(models.Model):
    userExercise = models.ForeignKey(UserExercises)
    setNumber = models.SmallIntegerField()
    reps = models.SmallIntegerField()

    class Meta:
        verbose_name = 'User\'s Exercise Reps'
        verbose_name_plural = 'User\'s Exercises Reps'

    def __unicode__(self):
        return str(self.reps)


class Session(models.Model):
    user = models.ForeignKey(User)
    sessionName = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'User\'s Exercise Session'
        verbose_name_plural = 'User\'s Exercise Session'

    def __unicode__(self):
        return str(self.sessionName)


class SessionDefaults(models.Model):
    session = models.ForeignKey(Session)
    isFixedReps = models.BooleanField(default=True)  # if this is false then it implies Weight is fixed but reps change

    class Meta:
        verbose_name = 'Session\'s Defaults'
        verbose_name_plural = 'Session\'s Defaults'

    def __unicode__(self):
        return str(self.isFixedReps)


class ExercisesInSession(models.Model):
    session = models.ForeignKey(Session)
    exercise = models.ForeignKey(UserExercises)

    class Meta:
        verbose_name = 'User\'s Exercises in Session'
        verbose_name_plural = 'User\'s Exercises in Session'

    def __unicode__(self):
        return str(self.session.sessionName)


class ExerciseSessionSchedule(models.Model):  # use date picker in front end which allows for easy picking of gym days
    session = models.ForeignKey(Session)
    chosenDays = models.DateField()

    class Meta:
        verbose_name = "User\'s Exercise Session Schedule"
        verbose_name_plural = 'User\'s Exercises Session Schedule'

    def __unicode__(self):
        return str(self.session.sessionName)
