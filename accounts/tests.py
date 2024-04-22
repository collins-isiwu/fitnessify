from django.test import TestCase
from rest_framework.test import APIClient

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_creation_valid_data(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'john',
            'last_name': 'Mark',
        }
        response = self.client.post('/api/v1/register/', data, format='json')
        self.assertEqual(response.status_code, 201)
