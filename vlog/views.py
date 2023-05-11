from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentsForm
from .models import Post, Comment
from django.views.decorators.http import require_POST
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
    comments=post.comments.filter(active=True)
    form=CommentsForm()
    return render(request,'blog/post/post_detail.html',{"post":post,"comments":comments,"form":form})

def post_share(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    sent=False
    form=EmailPostForm()

    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_uri=request.build_absolute_uri(post.get_absolute_path())
            subject=f"{cd['name']} recommends you to"\
                    f"{post_uri.title}"
            message=f"Read this {post.title} at {post_uri}"\
                    f"{cd['name']}\'s comment {cd['comments']}"
            send_mail(subject,message,'dansobaahkenneth@gmail.com',[cd['to']])
            sent=True
        else:
            form
    return render(request,'blog/post/post_share.html',{'post':post,'sent':sent,"form":form})




@require_POST
def post_comment(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    comment=None
    form = CommentsForm(data=request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post = post
        comment.save()
        print(comment.post)

    return render(request,'blog/post/comment.html',{'post':post,'comment':comment,'form':form})
