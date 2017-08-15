# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse, HttpResponse
import json
from models import *
from django.db.models import Q
from collections import defaultdict

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

    if request.method == 'GET':
        if request.GET['ExerciseName'] == "1":
            return_json = [exobj.as_json() for exobj in ExerciseName.objects.filter(isApproved=True)]
            return HttpResponse(json.dumps(return_json), content_type="application/json")
        if request.GET['MacroBody'] == "1":
            return_json = [exobj.as_json() for exobj in MacroBody.objects.all()]
            return JsonResponse(return_json)
        if request.GET['MicroBody'] == "1":
            return_json = [exobj.as_json() for exobj in MicroBody.objects.all()]
            return JsonResponse(return_json)

        if request.GET['ExerciseMuscleGroups'] == "1":  # ret muscle group and array of muscles incorporated in exercise
            exercise_muscle_groups = defaultdict(list)
            for result in ExerciseMuscleGroups.objects.all():
                exercise_muscle_groups[result['exerciseName']+"_micro"].append(result['targetMicro__microDesc'])
                exercise_muscle_groups[result['exerciseName']+"_macro"].append(result['targetMacro__macroDesc'])
            return JsonResponse(exercise_muscle_groups)

        if request.GET['ExerciseTipsForEx']:
            ex = request.GET['ExerciseTipsForEx']
            return_json = [exobj.as_json() for exobj in ExerciseTips.objects.filter(exerciseName=ex)]
            return JsonResponse(return_json)
        if request.GET['MicroBodyFilterBy']:  # user sends macro body part and gets associated micro parts
            part = request.GET['MicroBodyFilterBy']
            return_json = [exobj.as_json() for exobj in MicroBody.objects.filter(macroBody__macroDesc=part)]
            return JsonResponse(return_json)
        if request.GET['ExerciseMuscleGroupsFilterBy']:  # user sends macro body part and gets associated micro parts
            part = request.GET['ExerciseMuscleGroupsFilterBy']
            return_json = [exobj.as_json() for exobj in ExerciseMuscleGroups.objects.filter(Q(targetMicro__microDesc=part)) | Q(targetMacro__macroDesc=part)]
            return JsonResponse(return_json)
