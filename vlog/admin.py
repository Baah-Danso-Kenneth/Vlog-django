from django.contrib import admin
from vlog.models import  Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ['title','slug','author']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Comment)
