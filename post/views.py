from django.shortcuts import render, get_object_or_404, redirect
from .models import post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts=post.objects.all()
    return render(request, 'post/post_list.html',{'posts':posts})

def post_detail(request,pk):
    Post=get_object_or_404(post,pk=pk)
    return render(request,'post/post_detail.html',{'post':Post})

def create_post(request):
    myPost=post()
    User=request.user
    if request.method=='POST':
        myPost.title = request.POST.get('title')
        myPost.author = User
        myPost.content = request.POST.get('content')
        myPost.image = request.FILES.get('image',None)
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
        form = PostForm(request.POST, request.FILES, instance=curPost)
        if form.is_valid():
            updated_post=form.save(commit=False)
            updated_post.author=request.user
            updated_post.save()
            return redirect('post_detail',pk=curPost.pk)
        else:
            form=PostForm(instance=curPost)
        return render(request,'update_post.html',{'form':form})
    return render(
        request,
        'post/post_update.html',
        {
            'curPost' : curPost,
        },
    )

def delete_post(request, pk):
    delPost = get_object_or_404(post, pk=pk)
    delPost.delete()
    return redirect('post_list')