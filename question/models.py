# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=50, verbose_name=u'问题')
    answer = models.TextField(max_length=1000, verbose_name=u'回答')

    class Meta:
        verbose_name = '常见问题'
	verbose_name_plural = verbose_name
	db_table = 'question'

	def __uniclde__(self):
	    return self.question
