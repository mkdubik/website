from django.contrib import admin
from django.conf import settings

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    exclude = ('updated', 'icon',)

admin.site.register(Project, ProjectAdmin)

