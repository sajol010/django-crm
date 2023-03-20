from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client, RequestFactory
import json
# Create your tests here.

class UsersTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='admin', email='admin@admin.com', password='123456')
        self.client = Client()

    def test_user_authentication(self):

        """ Test authentication """
        response = self.client.post('/api/users/login', {
            'email': 'admin@admin.com',
            'password': '123456',
        })
        res = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['success'], True)
