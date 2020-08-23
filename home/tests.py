from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User

from home.models import Post

from home.views import two_buttons
from home.views import cv_view
from home.views import blog_view

class CVTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("Me", "me@me.com", "memememe")

    def tearDown(self):
        

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, two_buttons)

    def test_CV_url_resolves_correctly(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv_view)

    def test_blog_url_resolves_correctly(self):
        found = resolve('/blog')
        self.assertEqual(found.func, blog_view)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_has_correct_title(self):
        response = self.client.post('/')
        self.assertIn('<h2>My School CV thingy</h2>', response.content.decode())

    def test_home_has_two_buttons(self):
        response = self.client.post('/')

        self.assertIn('button', response.content.decode())

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("Me", "me@me.com", "memememe")

    def test_database_has_posts(self):
        post = Post()
        post.title = "Ahoy"
        post.text = "AaaaaaHooooYYYYY"
        post.author = self.user
        post.save()
        self.assertEqual(Post.objects.count(), 1)