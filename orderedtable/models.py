# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    s_no = models.IntegerField(null=True,blank=True)
    distance = models.IntegerField( null=False, blank=False)
    rate = models.IntegerField(null=False, blank=False)
    project_size = models.IntegerField(null=False, blank=False)
    completion_date = models.DateField(blank=False, null=False)