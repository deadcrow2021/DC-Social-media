from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=5000, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image= models.ImageField(default='post_default.jpg', upload_to='posts_pics')
    
    def __str__(self):
        return self.title
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)