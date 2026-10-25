from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.post = Post.objects.create(
            author=self.user,
            title='Test Title',
            text='Test Description'
        )

    def test_post_model(self):
        """Test model str representation and publish method"""
        self.assertEqual(str(self.post), 'Test Title')
        self.post.publish()

    def test_get_post_list(self):
        """Test retrieving list of posts"""
        response = self.client.get('/api_root/Post/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_301_MOVED_PERMANENTLY])

    def test_get_post_detail(self):
        """Test retrieving single post detail"""
        response = self.client.get(f'/api_root/Post/{self.post.id}/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_301_MOVED_PERMANENTLY])