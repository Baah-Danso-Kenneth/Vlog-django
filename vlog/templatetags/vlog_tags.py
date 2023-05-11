from django import template
from django.db.models import Count

from ..models import Post

register= template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.simple_tag
def show_latest_posts(count=5):
    return Post.objects.all()[:count]

@register.simple_tag
def get_most_commented_post(count=2):
    return Post.objects.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]