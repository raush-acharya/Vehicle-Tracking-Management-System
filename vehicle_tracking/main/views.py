from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def taskList(request):
    return HttpResponse("Vehicle Tracking")

def homePage(request):
    return render(request, 'index.html')

def otherPage(request):
    return render(request, 'other.html')

def featuresPage(request):
    return render(request, 'features.html')

def signUp(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')
        # return HttpResponse("user has been created successfully")
        # print(uname,email,pass1,pass2)
    return render(request, 'signup.html')

def logIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'login.html')

@login_required(login_url='login')
def dashBoard(request):
    return render(request, 'dashboard.html')

def logOut(request):
    logout(request)
    return redirect('login')

