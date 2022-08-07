from dataclasses import field 
from django import forms
from .models import comm, Comment, ReComment

class commForm(forms.ModelForm):
    class Meta:
        model = comm
        fields = ('title', 'text', 'img', 'file')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', )