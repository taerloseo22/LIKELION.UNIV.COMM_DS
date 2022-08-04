from django.db import models

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

