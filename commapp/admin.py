from django.contrib import admin
from .models import comm, Comment, ReComment, Commit

# Register your models here.

admin.site.register(comm)

admin.site.register(Comment)

admin.site.register(ReComment)

admin.site.register(Commit)
