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

    if request.method == 'GET':
        if 'ExerciseName' in request.GET:
            return_json = [exobj.as_json() for exobj in ExerciseName.objects.filter(isApproved=True)]
            return JsonResponse(return_json, safe=False)
        if 'MacroBody' in request.GET:
            return_json = [exobj.as_json() for exobj in MacroBody.objects.all()]
            return JsonResponse(return_json, safe=False)
        if 'MicroBody' in request.GET:
            return_json = [exobj.as_json() for exobj in MicroBody.objects.all()]
            return JsonResponse(return_json, safe=False)
        if 'MacroMicro' in request.GET:
            macro_micro = defaultdict(list)
            for exobj in MicroBody.objects.all():
                macro_micro[exobj.macroBody.macroDesc].append(exobj.microDesc)
            return JsonResponse(macro_micro, safe=False)

        if 'ExerciseMuscleGroups' in request.GET:  # ret muscle group and array of muscles incorporated in exercise
            exercise_muscle_groups = defaultdict(dict)

            for result in ExerciseMuscleGroups.objects.filter(exerciseName__isApproved=True):
                if result.targetMacro.macroDesc not in exercise_muscle_groups[result.exerciseName.exerciseName]:
                    exercise_muscle_groups[result.exerciseName.exerciseName][result.targetMacro.macroDesc] = [result.targetMicro.microDesc]
                else:
                    exercise_muscle_groups[result.exerciseName.exerciseName][result.targetMacro.macroDesc].append(result.targetMicro.microDesc)
            return JsonResponse(exercise_muscle_groups, safe=False)

        if 'ExerciseTipsForEx' in request.GET:
            ex = request.GET['ExerciseTipsForEx']
            return_json = [exobj.as_json() for exobj in ExerciseTips.objects.filter(exerciseName=ex)]
            return JsonResponse(return_json, safe=False)
        if 'MicroBodyFilterBy' in request.GET:  # user sends macro body part and gets associated micro parts
            part = request.GET['MicroBodyFilterBy']
            return_json = [exobj.as_json() for exobj in MicroBody.objects.filter(macroBody__macroDesc=part)]
            return JsonResponse(return_json, safe=False)
        if 'ExerciseMuscleGroupsFilterBy' in request.GET:  # user sends macro body part and gets associated micro parts
            part = request.GET['ExerciseMuscleGroupsFilterBy']
            return_json = [exobj.as_json() for exobj in ExerciseMuscleGroups.objects.filter(Q(targetMicro__microDesc=part)) | Q(targetMacro__macroDesc=part)]
            return JsonResponse(return_json, safe=False)
