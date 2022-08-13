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
                'style': 'max-width: 300px;',
                'placeholder': '제목을 입력하세요'
                }),
            'text': forms.TextInput(attrs={
                'class': "form-textarea",
                'placeholder': '여러분의 이야기를 적어주세요'
                }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', )