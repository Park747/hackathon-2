from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
import json
from django.http import HttpResponse,JsonResponse
from .models import User, Profile, Review
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : '존재하지 않는 아이디/비밀번호 입니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            nickname = request.POST["nickname"]
            address = request.POST["address"]
            catspecies = request.POST["catspecies"]
            catnumber = request.POST["catnumber"]
            catimage = request.POST["catimage"]
            userimage = request.POST["userimage"]
            profile = Profile(
                user=user, 
                nickname=nickname,
                address=address,
                catspecies=catspecies,
                catnumber=catnumber,
                catimage=catimage,
                userimage=userimage
            )
            profile.save()
            auth.login(request,user)
            return redirect('home')
    return render(request, 'register.html')

def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'my_profile.html', {'profile' : profile})

@csrf_exempt
def personal_detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    profile = Profile.objects.get(user=user)
    reviews = Review.objects.filter(profile=user)
    if request.method == "POST":
        reviewer = request.user
        text = request.POST["review"]
        Review.objects.create(
            reviewer = reviewer,
            profile = user,
            text = text
        )
        return redirect('personal_detail', user.pk)
    return render(request, 'personal_detail.html', {'profile' : profile, 'reviews' : reviews})


def personal_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        new_profile = profile.update(
            nickname = request.POST["nickname"],
            address = request.POST["address"],
            catspecies = request.POST["catspecies"],
            catnumber = request.POST["catnumber"],
            catimage = request.POST["catimage"],
            userimage = request.POST["userimage"]
        )
        new_profile.save()
        return redirect('home')
    return render(request, 'personal_edit.html', {'profile' : profile})

