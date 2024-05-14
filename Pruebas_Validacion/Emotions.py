import unittest
import requests

class TestEmotions(unittest.TestCase):
    def test_get_emotions_happy(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_emotions'
        params = {'text': 'The food was super good would recommend to everyone'}

        response = requests.get(url, params=params)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], '5')


    def test_get_emotions_sad(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_emotions'
        params = {'text': 'Really awful experience, would not recommend to anyone. Worst food ever.'}

        response = requests.get(url, params=params)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], '1')


    def test_get_emotions_neutral(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_emotions'
        params = {'text': 'The was normal, nothing special about it. It was better than expected.'}

        response = requests.get(url, params=params)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'], '3')

if __name__ == '__main__':
    unittest.main()