from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from .forms import SignupForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from post.models import post
from comment.models import comment

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


from .models import user as User

#Create your views here.
def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            User=auth.authenticate(username=username,password=raw_password)
            auth.login(request,User)
            return redirect('post_list')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request,error)
            return redirect('signup')
    else:
        form=SignupForm()
    return render(request, 'account/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            User=auth.authenticate(
                request=request,
                username=username,
                password=password
            )
            if User is not None:
                auth.login(request, User)
                return redirect('post_list')
            return redirect('login')
    else:
        form=AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('post_list')

def delete(request):
    User=request.user
    User.delete()
    return redirect('post_list')

def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form=CustomUserChangeForm(instance=request.user)
    return render(request, 'account/update.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('post_list')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html',{'form':form})

def user_info(request):
    session=request.COOKIES['sessionid']
    session = request.COOKIES['sessionid']
    session = Session.objects.get(session_key=session)
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id')
    user = User.objects.get(id=uid)
    posts=post.objects.filter(author=user)
    comments=comment.objects.filter(author=user)
    return render(request,'account/userinfo.html',{'user':user,'posts':posts, 'comments':comments})