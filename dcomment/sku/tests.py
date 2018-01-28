import uuid

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


from .models import Comment



class CommentModelTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.comment_sku = uuid.uuid1()
        self.comment_content = "This is comment."
        self.comment = Comment(sku=self.comment_sku, content=self.comment_content)

    def test_model_can_create_a_comment(self):
        old_count = Comment.objects.count()
        self.comment.save()
        new_count = Comment.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_do_tone(self):
        self.comment.save()
        self.assertNotEqual(self.comment.tone, '')


class CommentViewTestCase(TestCase):
    """Test suite for the api views."""
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_superuser('admin', 'admin@none.no', 'admin')
        self.client.force_authenticate(user=user)

        self.comment_data = {
            'sku': uuid.uuid1(),
            'content': "This is an interesting comment."
        } 

        self.response = self.client.post(
            '/comments/',
            self.comment_data,
            format="json"
        )
    
    def test_api_can_create_a_comment(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)