# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Blog(models.Model):
    blog_name = models.CharField(max_length=20, unique=True, error_messages={
            'unique': _("A blog with that blog name already exists."),
        },)
    blog_content = models.CharField(max_length=150)
    date_creared = models.DateTimeField(_('date joined'), default=timezone.now)
    is_published = models.BooleanField(default=False)
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.blog_name
    
