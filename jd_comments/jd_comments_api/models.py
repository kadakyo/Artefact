# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
	content = models.CharField(max_length=200)
	creationTime = models.DateTimeField()
	nickname = models.CharField(max_length=200)
	score = models.CharField(max_length=200)
