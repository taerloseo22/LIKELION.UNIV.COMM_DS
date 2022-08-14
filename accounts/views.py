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
                last_name = request.POST['last_name'],
            )
            auth.login(request, user)
            return redirect('board')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

