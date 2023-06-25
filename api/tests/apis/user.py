from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-list')

    def test_list_users(self):
        user1 = User.objects.create(first_name='Oswald', last_name="Gyabaah", email='user1@example.com', password='password')
        user2 = User.objects.create(first_name="Another", last_name="User", email='user2@example.com', password='password')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['username'], user1.username)
        self.assertEqual(response.data[1]['email'], user2.email)
