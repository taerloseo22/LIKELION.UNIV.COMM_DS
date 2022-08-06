from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class comm(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    img = models.ImageField(blank=True, null=True, upload_to='lion_photo/%y/%m/%d/')
    file = models.FileField(blank=True, null=True,upload_to='lion_file/%y/%m/%d/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(comm, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

class ReComment(models.Model):
    post = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField("🐾",max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post





