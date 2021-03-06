from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
