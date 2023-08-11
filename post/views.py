from django.shortcuts import render, get_object_or_404, redirect
from .models import post, Category
from .forms import PostForm
from comment.models import comment
from django.db.models import Q

# Create your views here.
def post_list(request):
    posts=post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    print(categories)
    return render(request, 'post/post_list.html',{'posts':posts, 'categories':categories})

def post_detail(request,pk):
    Post=get_object_or_404(post,pk=pk)
    if request.method == "POST":
        myComment=comment()
        User=request.user
        myComment.post=Post
        myComment.author=User
        myComment.content=request.POST.get('content')
        if myComment.content:
            myComment.save()
    comments=comment.objects.filter(post=pk)
    count=comments.count()
    return render(request,'post/post_detail.html',{'post':Post, 'comments':comments, 'count':count})

def create_post(request):
    myPost=post()
    User=request.user
    if request.method=='POST':
        myPost.title = request.POST.get('title')
        myPost.author = User
        myPost.content = request.POST.get('content')
        myPost.image = request.FILES.get('image',None)
        category_num = request.POST.get('category')
        category = Category.objects.get(id=category_num)
        myPost.category = category
        if myPost.title and myPost.content:
            myPost.save()
            return redirect('post_list')
    else:
        form=PostForm()
    return render(
        request,
        'post/post_create.html', {'form':form}
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
        return render(request,'post/update_post.html',{'form':form})
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

def search(request):
    posts = post.objects.all().order_by("-created_at")
    search = request.GET.get('search','')
    if search:
        search_list = posts.filter(
            Q(title__icontains = search)|
            Q(content__icontains = search)
        )
    return render(request, 'post/search.html', {'posts':search_list, 'search': search})

def category_view(request, category_slug):
    category=get_object_or_404(Category, slug=category_slug)
    category=Category.objects.get(slug=category_slug)
    category_posts=post.objects.filter(category=category)
    categories=Category.objects.all()
    return render(request, "post/post_list.html",{"category":category, "posts":category_posts, "categories":categories})