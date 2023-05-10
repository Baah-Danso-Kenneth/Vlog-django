from django.contrib import admin
from vlog.models import  Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['title','slug','author']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Comment)
