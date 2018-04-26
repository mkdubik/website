from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    excluded = ('slug',)


admin.site.register(Post, PostAdmin)


# Register your models here.
