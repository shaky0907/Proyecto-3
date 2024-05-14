import unittest
import requests

class TestMenu(unittest.TestCase):

    def test_get_menu(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_menu'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'][0]['dish']['name'], "Filete de res")

    

if __name__ == '__main__':
    unittest.main()