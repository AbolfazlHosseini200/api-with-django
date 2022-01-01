from django.test import TestCase
from django.test.client import Client
from rest_framework.utils import json


class UrlTest(TestCase):
    def test_register(self):
        jsons = {
            "first_name": "abolfazl",
            "last_name": "hosseini",
            "number": "fake@email",
            "password": "1234",
            "password2": "1234",
            "username": "abolfazl81"
        }
        response = self.client.post('/register/', json.dumps(jsons), 'json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        jsons = {
            "token": "",
        }
        response = self.client.post('/logout/', json.dumps(jsons), 'json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        jsons = {
            "username": "abolfazl81",
            "password": "1234"
        }
        response = self.client.post('/login/', json.dumps(jsons), 'json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        self.assertEqual(response.status_code, 200)

    def test_insurance(self):
        jsons = {
            "age": "20",
            "email": "1234",
            "smoke": 'False',
            "bmi": "25.0",
            "token": ""
        }
        response = self.client.post('/insurance/', json.dumps(jsons), 'json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest', )
        self.assertEqual(response.status_code, 200)
