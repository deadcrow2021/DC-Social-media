from django.contrib.auth.models import User
from django.test import TestCase, Client
from users.models import Profile
from users.forms import EditProfile


class TestPostView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.profile = Profile.objects.filter(id=1).first()
        self.client.login(username='test_user', password='test_pass')


    def test_edit_profie_form(self):
        form = EditProfile(data={
            'username': 'test_username',
            'email': 'test_email@gmail.com',
            'first_name': 'test',
            'last_name': 'test1'
        })
        
        self.assertTrue(form.is_valid())


    def test_edit_profie_form_no_data(self):
        form = EditProfile(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)