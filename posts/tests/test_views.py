from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from users.models import Profile
from posts.models import Post


class TestPostView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.profile = Profile.objects.filter(id=1).first()
        self.client.login(username='test_user', password='test_pass')


    def test_home_view_GET(self):
        req = self.client.get(reverse('index'))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'posts/index.html')


    def test_create_post_view_GET(self):
        req = self.client.get(reverse('create-post'))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'posts/create_post.html')

    def test_create_post_view_POST(self):
        req = self.client.post(reverse('create-post'), {
            'title': 'test_title',
            'text': 'test_text',
        })
        self.assertEqual(req.status_code, 302)
        self.assertEqual(self.profile.posts.first().title, 'test_title')


    def test_post_view_GET(self):
        post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')
        req = self.client.get(reverse('post', args=['1']))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'posts/post.html')


    def test_update_post_view_GET(self):
        post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')
        req = self.client.get(reverse('update-post', args=['1']))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'posts/update_post.html')

    def test_update_post_view_POST(self):
        post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')
        req = self.client.post(reverse('update-post', args=['1']), {
                'title': 'test_title_new',
                'text': 'test_text_new',
            })
        self.assertEqual(req.status_code, 302)
        self.assertEqual(self.profile.posts.first().title, 'test_title_new')


    def test_delete_post_view_GET(self):
        post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')
        req = self.client.get(reverse('delete-post', args=[1]))
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'posts/delete_post.html')

    def test_delete_post_view_POST(self):
        post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')
        req = self.client.post(reverse('delete-post', args=[1]), {'id':1})
        self.assertEqual(req.status_code, 302)
        self.assertEqual(self.profile.posts.count(), 0)
        
    def test_delete_post_view_POST_no_id(self):
        post = Post.objects.create(author=Profile.objects.filter(id=1).first(),
                                        title='test_title', text='test_text')
        req = self.client.post(reverse('delete-post', args=[1]))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(self.profile.posts.count(), 1)

