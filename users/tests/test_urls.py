from users.views import profile, edit_profile, login_user, logout_user, register_user, subscribers_posts
from django.urls import resolve, reverse
from django.test import TestCase


class TestExample(TestCase):
    
    def test_url_profile_page(self):
        url = reverse('profile', args=[1])
        self.assertEqual(resolve(url).func, profile)
    
    def test_url_edit_profile_page(self):
        url = reverse('edit-profile', args=[1])
        self.assertEqual(resolve(url).func, edit_profile)
        
    def test_url_login_page(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_user)

    def test_url_logout_page(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_url_register_page(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_user)

    def test_url_subscriptions_page(self):
        url = reverse('subscriptions')
        self.assertEqual(resolve(url).func, subscribers_posts)
