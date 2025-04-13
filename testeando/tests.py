from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from pprint import pprint

class TestLogin(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'juanp',
            'password': 'df3S$fw2332G',
            'first_name': 'Juanito',
            'last_name': 'Perez',
            'email': 'juanpPerez@gmail.com'
        }
        # Crear usuario
        self.client.post(reverse('register'), self.user_data)

    def test_login(self):
        response = self.client.post(reverse('login'), data={
            'username': 'juanp',
            'password': 'df3S$fw2332G'
        })

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

