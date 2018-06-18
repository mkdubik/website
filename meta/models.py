from django.db import models

from datetime import datetime


class Project(models.Model):
    started = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated = models.DateTimeField(blank=False, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    git = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return ''.join([self.title,' - ',self.updated.strftime("%A, %d. %B %Y %I:%M%p") if self.updated else self.started.strftime("%A, %d. %B %Y %I:%M%p")])
