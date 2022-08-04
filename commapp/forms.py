from django import forms
from .models import comm

class commForm(forms.ModelForm):
    class Meta:
        model = comm
        fields = ('title', 'text', 'img', 'file')