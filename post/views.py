from django.shortcuts import render, get_object_or_404, redirect
from .models import post


# Create your views here.
def post_list(request):
    posts=post.objects.all()
    return render(request, 'post/post_list.html',{'posts':posts})

def post_detail(request,pk):
    Post=get_object_or_404(post,pk=pk)
    return render(request,'post/post_detail.html',{'post':Post})

def create_post(request):
    myPost=post()
    if request.method=='POST':
        myPost.title = request.POST.get('title')
        myPost.author = request.POST.get('author','')
        myPost.content = request.POST.get('content')
        myPost.image = request.POST.get('image',None)
        if myPost.title and myPost.content:
            myPost.save()
            return redirect('post_list')
    return render(
        request,
        'post/post_create.html'
    )
    
def update_post(request, pk):
    curPost = get_object_or_404(post, pk=pk)
    if request.method=='POST':
        curPost.title = request.POST.get('title')
        curPost.author = request.POST.get('author','')
        curPost.content = request.POST.get('content')
        curPost.image = request.POST.get('image',None)
        if curPost.title and curPost.content:
            curPost.save()
            return redirect('post_list')
    return render(
        request,
        'post/post_update.html',
        {
            'curPost' : curPost,
        },
    )