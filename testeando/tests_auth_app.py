from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

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
        print("Justo aqui")
        # Crear usuario
        response = self.client.post(reverse('register_user'), self.user_data)

        print("El estado de la solicitud con POST es: ", response.status_code)


    def test_login(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'username': 'juanp',
                'password': 'df3S$fw2332G'
            },
            content_type="application/json"
        )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)


    def test_token_refresh(self):
        response01 = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'username': 'juanp',
                'password': 'df3S$fw2332G'
            },
            content_type="application/json"
        )

        response02 = self.client.post(
            reverse('token_refresh'),
            data={
                'refresh': response01.json()['refresh']
            },
            content_type="application/json"
        )

        print(response02.json())

        self.assertEqual(response02.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response02.data)
        self.assertIn('access', response02.data)


    def test_logout(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'username': 'juanp',
                'password': 'df3S$fw2332G'
            },
            content_type="application/json"
        )
        token_refresh = response.json()['refresh']

        print("El inicio de sesion fue:", response.status_code)

        response1 = self.client.post(
            reverse('revocar_token'),
            data={
                'refresh': token_refresh
            },
            content_type="application/json"
        )

        print("La revocacion del token fue:", response.status_code)

        response2 = self.client.post(
            reverse('token_refresh'),
            data={'refresh': token_refresh},
            content_type='application/json'
        )

        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)