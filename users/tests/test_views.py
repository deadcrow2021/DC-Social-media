from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from users.models import Profile


class TestPostView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.profile = Profile.objects.filter(id=1).first()
        self.client.login(username='test_user', password='test_pass')


    def test_profile_view_GET(self):
        req = self.client.get(reverse('profile', args=['1']))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'users/profile.html')


    def test_edit_profile_view_GET(self):
        req = self.client.get(reverse('edit-profile', args=['1']))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'users/edit_profile.html')


    def test_login_view_GET(self):
        req = self.client.get(reverse('login'))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'users/login.html')


    def test_logout_view_GET(self):
        req = self.client.get(reverse('logout'))
        self.assertEqual(req.status_code, 302)


    def test_register_view_GET(self):
        req = self.client.get(reverse('register'))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'users/register.html')


    def test_subscriptions_view_GET(self):
        req = self.client.get(reverse('subscriptions'))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'users/subscriptions.html')
