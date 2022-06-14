import unittest

from flask import request
from index import principal
import unittest
import requests

class probar(unittest.TestCase):
    PRINCIPAL_URL = "http://localhost:9696"

    def test_principal(self):
        b = requests.get(probar.PRINCIPAL_URL)
        self.assertEqual(b.status_code,200)
        #self.assertEqual(len(b.json()),1)
        print("Todo bien")

    

if __name__ == "__main__":
    probador = probar()
    probador.test_principal()
