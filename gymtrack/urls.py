"""gymtrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import exercises.views as ex_view
import usertrack.views as user_views

admin.site.index_title = 'Gym Planner Administration'
admin.site.site_header = 'Gym Planner Administration'
admin.site.site_title = 'Gym Planner Admin'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),

    url(r'^exercise_manager/$', ex_view.exercise_handler),

    url(r'^user_manager/$', user_views.user_handling),
    url(r'^$', user_views.homepage),
]
