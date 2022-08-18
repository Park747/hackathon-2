import profile
from django.shortcuts import render, redirect
from .models import Post,User,Comment
from django.contrib.auth.decorators import login_required 
from django.contrib import auth
from django.contrib.auth import authenticate
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'home.html')

def community_home(request):
    posts = Post.objects.all()
    return render(request, 'community_home.html', {'posts':posts})

@login_required(login_url="user/login/")
def community_new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            author = request.user,
            profile = request.user.profile,
            title = request.POST["title"],
            category = request.POST["category"],
            body = request.POST["body"],
            image = request.POST["image"],
        )
        new_post.save()
        return redirect('community_detail', new_post.pk)
    return render(request, 'community_new.html')

@login_required(login_url="/login")
def community_detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.numberview += 1
    post.save()
    if request.method == "POST":
        author = request.user
        profile = request.user.profile
        text = request.POST["text"]
        Comment.objects.create(
            author = author,
            profile = profile,
            post = post,
            text = text,
        )
        return redirect('community_detail', post.pk)
    return render(request, 'community_detail.html', {'post' : post})
    
def community_edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == "POST":
        post = Post.objects.filter(pk = post_pk).update(
            author = request.user,
            profile = request.user.profile,
            title = request.POST["title"],
            category = request.POST["category"],
            body = request.POST["body"],
            image = request.POST["image"],
        )
        return redirect('community_home')
    return render(request, 'community_edit.html' , {'post' : post})

def community_delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('community_home')



   
