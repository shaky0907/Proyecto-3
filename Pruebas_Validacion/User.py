import unittest
import requests

class TestUser(unittest.TestCase):
    def test_login(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/login'
        body = {
            'contrasena': 'clave123',
            'correo': 'usuario1@example.com'
        }

        response = requests.post(url, json=body)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "data": {
                "correct": True,
                "id": 1
            },
            "status": 200,
            "status_code": 200
        }
        self.assertEqual(response.json(), expected_response)


    def test_login_bad(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/login'
        body = {
            'contrasena': 'No es la clave correcta',
            'correo': 'usuario1@example.com'
        }

        response = requests.post(url, json=body)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "data": {
                "correct": False,
                "id": 0
            },
            "status": 200,
            "status_code": 200
        }
        self.assertEqual(response.json(), expected_response)

    """
    def test_add_user(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/add_user'
        body = {
            'contrasena': 'test_password',
            'correo': 'test_email@example.com',
            'nombre': 'Test',
            'apellido': 'User',
            'direccion': 'Test Address',
            'nivel_acceso': 1
        }

        response = requests.post(url, json=body)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
    """


    def test_get_user_id(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_user_id'
        params = {'id': 1}

        response = requests.get(url, params=params)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['correo'], 'usuario1@example.com')
        self.assertEqual(response.json()['data']['id'], 1)

    def test_update_password(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/update_password'
        body = {
            'correo': "usuario1@example.com",
            'contrasena': 'clave123'
        }

        response = requests.post(url, json=body)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)

    


if __name__ == '__main__':
    unittest.main()