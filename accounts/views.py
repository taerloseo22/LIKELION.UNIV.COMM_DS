
from django.shortcuts import render,redirect
# from accounts.forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
                email = request.POST['email'],
            )
            auth.login(request, user)
            return redirect('board')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("board")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(requset):
    auth.logout(requset)
    return redirect('board')       

