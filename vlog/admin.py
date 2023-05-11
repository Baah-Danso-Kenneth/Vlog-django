from django.contrib import admin
from vlog.models import  Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['title','slug','author']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created','active']
    list_filter=['active','created','updated']
    search_fields = ['post','name']
    pass
# admin.site.register(Comment)
