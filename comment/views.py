from django.shortcuts import render, redirect, get_object_or_404
from .models import comment
from post.models import post
from .forms import PostComment

# Create your views here.
def update_comment(request, postpk, commentpk):
    curComment=get_object_or_404(comment,pk=commentpk)
    curPost=get_object_or_404(post, pk=postpk)
    if request.method=='POST':
        curComment.content=request.POST['content']
        curComment.save()
        return redirect('post_detail',pk=curPost.pk)
    return render(request,'comment/comment_update.html',{'curComment':curComment})

def delete_comment(request, postpk, commentpk):
    curPost=get_object_or_404(post,pk=postpk)
    delComment = get_object_or_404(comment, pk=commentpk)
    delComment.delete()
    return redirect('post_detail', pk=curPost.pk)