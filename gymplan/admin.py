# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

admin.site.register(UserExercises)
admin.site.register(UserExercisesSetReps)
admin.site.register(SessionDefaults)
admin.site.register(Session)
admin.site.register(ExercisesInSession)
admin.site.register(ExerciseSessionSchedule)
