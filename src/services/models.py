# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Blog(models.Model):
    blog_name = models.CharField(max_length=20, unique=True, error_messages={
            'unique': _("A blog with that blog already exists."),
        },)
    blog_content = models.CharField(max_length=150)
    blog_user = models.CharField(max_length=150)
    
    date_creared = models.DateTimeField(_('date joined'), default=timezone.now)
    
    def __str__(self):
        return self.blog_name
    
