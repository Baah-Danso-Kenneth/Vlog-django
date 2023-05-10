from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment

# Create your views here.
def post_list(request):
    post_list= Post.objects.all()
    paginator= Paginator(post_list,3)
    page_number=request.GET.get('page',1)

    try:
        posts=paginator.page(page_number)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        paginator.page(1)

    return render(request,'blog/post/post_list.html',{"posts":posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post/post_detail.html',{"post":post})
