# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse, HttpResponse

from models import *
from django.db.models import Q
from collections import defaultdict

from django.shortcuts import render
from pprint import pprint
import json, datetime

@login_required
def session_handler(request):
    if request.method == 'POST':  # handler for when request is first made
        if request.POST.get('CreateSession', 0):
            Session.objects.create(user=request.user, sessionName=request.POST.get('sessionName', ''))

        else:
            session = Session.objects.get(user=request.user, sessionName=request.POST.get('sessionName', ''))
            if request.POST.get('CreateSessionExercise', 0):
                exercise = UserExercises.objects.get(user=request.user,
                                                     exercise__exerciseName=request.POST.get('exerciseName', ''))
                ExercisesInSession.objects.create(session=session, exercise=exercise)
            if request.POST.get('CreateSessionSchedule', 0):
                date_list = json.loads(request.POST.get('sessionDates', 0))
                for date in date_list:
                    date_obj = datetime.datetime.strptime(date, "%d-%m-%Y").date()
                    ExerciseSessionSchedule.objects.create(session=session, chosenDays=date_obj)


@login_required
def user_exercise_handler(request):
    if request.method == 'POST':
        exercise = ExerciseName.objects.get(exerciseName=request.POST.get('exerciseName', ''))
        if request.POST.get('CreateUserExercise', 0):
            UserExercises.objects.create(user=request.user, exercise=exercise)
        else:
            exercise = UserExercises.objects.get(user=request.uesr, exercise=exercise)
            if request.POST.get('CreateExerciseDetails', 0):
                reps = json.loads(request.POST.get('exerciseReps', 0))
                for i in enumerate(reps):
                    UserExercisesSetReps.objects.create(userExercise=exercise, setNumber=i, reps=reps[i])
                pass
