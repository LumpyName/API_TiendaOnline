from pprint import pprint

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
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

    def loguearse(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'username': 'juanp',
                'password': 'df3S$fw2332G'
            },
            content_type="application/json"
        )

        return {
            'status_code': response.status_code,
            'refresh': response.json()['refresh'],
            'access':  response.json()['access'],
            'json': response.json()
        }

    def test_prueba(self):
        token_access = self.loguearse()['access']

        response = self.client.put(
            reverse('prueba'),
            data={
                'access_token': token_access,
                'first_name': "Juan",
                'last_name': "Peres Llupanqui"
            },
            content_type="application/json"
        )

        pprint(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_token_refresh(self):
        token_refresh = self.loguearse()['refresh']

        response = self.client.post(
            reverse('token_refresh'),
            data={
                'refresh': token_refresh
            },
            content_type="application/json"
        )

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)


    def test_logout(self):
        token_refresh = self.loguearse()['refresh']
        response_status_code = self.loguearse()['status_code']

        print("El inicio de sesion fue:", response_status_code)

        response = self.client.post(
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