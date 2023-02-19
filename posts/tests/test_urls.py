from posts.views import home, post, update_post, delete_post, create_post
from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase
from users.models import Profile
from posts.models import Post


class TestPostUrl(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test_user')
        self.post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')

    
    def test_url_home_page(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, home)

    def test_url_post_page(self):
        url = reverse('post', args=[1])
        self.assertEqual(resolve(url).func, post)

    def test_url_update_post_page(self):
        url = reverse('update-post', args=[1])
        self.assertEqual(resolve(url).func, update_post)

    def test_url_delete_post_page(self):
        url = reverse('delete-post', args=[1])
        self.assertEqual(resolve(url).func, delete_post)

    def test_url_create_post_page(self):
        url = reverse('create-post')
        self.assertEqual(resolve(url).func, create_post)
