from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True)
    image = models.ImageField(default='profile_default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        if img.height > 1920 or img.width > 1080:
            output_size = (1920, 1080)
            img.thumbnail(output_size)
            img.save(self.image.path)