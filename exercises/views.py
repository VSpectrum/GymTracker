# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from models import *
from django.shortcuts import render


@user_passes_test(lambda u: u.is_superuser)
def body_create_handler(request):
    if request.method == 'POST':  # handler for when request is first made
        if request.POST.get('MacroBody', 0):
            MacroBody.objects.create(macroDesc=request.POST.get('macroDesc', ''))

        if request.POST.get('MicroBody', 0):
            macro_body = MacroBody.objects.get(macroDesc=request.POST.get('macroDesc', ''))
            MicroBody.objects.create(macroBody=macro_body, microDesc=request.POST.get('microDesc', ''))


@login_required
def exercise_handler(request):
    if request.method == 'POST':
        if request.POST.get('ExerciseName', 0):
            ExerciseName.objects.create(exerciseName=request.POST.get('exerciseName', ''))

        if request.POST.get('ExerciseMuscleGroups', 0):
            ex_name = ExerciseName.objects.get(exerciseName=request.POST.get('exerciseName', ''))
            macro_body = MacroBody.objects.get(macroDesc=request.POST.get('macroDesc', ''))
            micro_body = MicroBody.objects.get(macroBod=macro_body, microDesc=request.POST.get('microDesc', ''))
            ExerciseMuscleGroups.objects.create(exerciseName=ex_name, targetMacro=macro_body, targetMicro=micro_body)

        if request.POST.get('ExerciseTips', 0):
            ex_name = ExerciseName.objects.get(exerciseName=request.POST.get('exerciseName', ''))
            ExerciseTips.objects.create(exerciseName=ex_name, exerciseTip=request.POST.get('exerciseTip', ''))