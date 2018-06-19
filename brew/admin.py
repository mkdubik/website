from django.contrib import admin

from .models import Log
from .models import LogEntry
from django.utils.text import slugify

class LogAdmin(admin.ModelAdmin):
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.brew_type) + '/' + obj.yeast_addition.strftime('%Y/%m/%d')
        super().save_model(request, obj, form, change)

class LogEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Log, LogAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
