import unittest
import requests

class TestReservation(unittest.TestCase):

    def test_get_reservation(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_reservation'
      

        response = requests.get(url)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)

     
    """
    def test_add_reservation(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/add_reservation'
        body = {
            "time": "10:00",
            "date": "2021-10-10",
            "state": 1,
            "people_quant": 2,
            "id_user": 1
        }
        response = requests.post(url, json=body)
        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
        
    """
    def test_edit_reservation(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/edit_reservation'
        body = {
            'id': 1,
            'state': 1,
            'people_quant': 3,
            'id_user': 1
        }

        response = requests.post(url, json=body)

        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)


    def test_get_reservation_per_user(self):
        url = 'https://us-central1-proyectosoa-422123.cloudfunctions.net/get_reservation_per_user'
        params = {'id': 1}

        response = requests.get(url, params=params)
        print(response.json())
        # Check that the response is as expected
        self.assertEqual(response.status_code, 200)
    
        #check if the length of data array is 5
        self.assertEqual(len(response.json()['data']), 3)

    

if __name__ == '__main__':
    unittest.main()