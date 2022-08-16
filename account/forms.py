from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class signupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1',"password2",'nickname']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': '아이디'
                }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': '영문, 숫자, 특수문자로 구성된 6~20자 비밀번호'
                }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': '비밀번호 재입력'
                }),
            'nickname': forms.TextInput(attrs={
                'placeholder': '이름'
                }),
        }