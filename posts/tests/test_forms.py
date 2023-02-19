from django.contrib.auth.models import User
from django.test import TestCase, Client
from users.models import Profile
from posts.forms import CreateUpdatePost


class TestPostView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.profile = Profile.objects.filter(id=1).first()
        self.client.login(username='test_user', password='test_pass')


    def test_create_update_post_form(self):
        form = CreateUpdatePost(data={
            'title': 'test_title',
            'text': 'test_text'
        })
        
        self.assertTrue(form.is_valid())
