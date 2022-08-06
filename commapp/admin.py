from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import comm, Comment, ReComment

# Register your models here.

admin.site.register(comm)

admin.site.register(Comment)

admin.site.register(ReComment)