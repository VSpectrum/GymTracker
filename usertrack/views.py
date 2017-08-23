# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, JsonResponse, HttpResponseServerError, HttpResponseBadRequest


def user_handling(request):  # handles posts to determine user registration, logging in, and logging out
    if request.method == "POST":
        if request.POST.get('log_in', 0):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect("/")
                    # requestUser = UserProfile.objects.get(user=user)
                    # if requestUser.isVerified:
                    #     auth_login(request, user)
                    #     return redirect("/")
                    # else:
                    #     return HttpResponse('User is not verified via email')
                else:
                    return HttpResponse('User is disabled.')
            else:
                return HttpResponse('Username does not exist.')
        elif request.POST.get('registration', 0):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            # check if email unique, check if username unique
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                            password=password)
            # send email verification ?
            return redirect('/')
        elif request.POST.get('log_out', 0):
            auth_logout(request)
            return redirect('/')


def homepage(request):
    if request.user.is_authenticated():
        logged_user = User.objects.get(username=request.user)
        data = {
        }
        return render(request, 'home.html', data)
    else:
        return render(request, 'index.html')
