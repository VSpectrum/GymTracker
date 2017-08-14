# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


def user_image_folder(instance, filename):
    return "%s/%s" % (instance.user.username, filename)


class UserProgressPics(models.Model):
    user = models.ForeignKey(User)
    pic = models.ImageField(upload_to=user_image_folder, default='pic_folder/None/no-img.jpg')

    class Meta:
        verbose_name = 'Progress Pictures'
        verbose_name_plural = 'Progress Pictures'

    def __unicode__(self):
        return str(self.user.username)
