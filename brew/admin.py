from django.contrib import admin

from .models import Log
from .models import LogEntry

class LogAdmin(admin.ModelAdmin):
    pass

class LogEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Log, LogAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
