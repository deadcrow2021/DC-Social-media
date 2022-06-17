from django.forms import ModelForm
from .models import Post

class CreateUpdatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
