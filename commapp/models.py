from django.db import models
from commprj import settings
from account.models import CustomUser
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
# from django.contrib.auth.models import User

# Create your models here.
# User = settings.AUTH_USER_MODEL
class comm(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # title = models.CharField('',max_length=50)
    # author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    text = MarkdownxField()
    img = models.ImageField(blank=True, null=True, upload_to='lion_photo/%y/%m/%d/')
    file = models.FileField(blank=True, null=True,upload_to='lion_file/%y/%m/%d/')
    OPTION = (
        ('talk','TALK'),
        ('issue','ISSUE'),
        ('project','PROJECT'),
        ('connent','CONNENT'),
    )
    tag = models.CharField(max_length=7, choices=OPTION)

    def __str__(self):
        return self.title

    def get_content_markdown(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(comm, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}::{self.content}'

class ReComment(models.Model):
    post = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.CharField("🐾",max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class Commit(models.Model):
    user = models.ForeignKey(CustomUser, related_name = "userof", on_delete=models.CASCADE)
    gitName = models.CharField(max_length=50)
    commit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.gitName}'



