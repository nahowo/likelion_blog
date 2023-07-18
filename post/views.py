from django.shortcuts import render, get_object_or_404
from .models import post


# Create your views here.
def post_list(request):
    posts=post.objects.all()
    return render(request, 'post/post_list.html',{'posts':posts})

def post_detail(request,pk):
    Post=get_object_or_404(post,pk=pk)
    return render(request,'post/post_detail.html',{'post':Post})

def create_post(request):
    return render(
        request,
        'post/post_create.html'
    )