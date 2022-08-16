from dataclasses import field 
from django import forms
from .models import comm, Comment, ReComment

class commForm(forms.ModelForm):
    class Meta:
        model = comm
        fields = ('title','tag','text', 'img', 'file')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 90%',
                'placeholder': '제목을 입력하세요'
                }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': "commentform",
                'placeholder': '댓글을 작성하세요'
                }),
        }


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', )

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(label="likelion 이메일")
#     github_email = forms.EmailField(label="github 아이디")
#     class Meta:
#         model = User
#         fields = ['username','password1','password2','github_email', 'email']

# class loginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email','password1']