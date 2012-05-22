"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class UserFunctionTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration(self):
        response = self.client.post('/regis/', {'username': 'demo', 'password': '123456' , 'email':'demo123456@mail.com'})
        self.assertEqual(response.status_code, 302)
