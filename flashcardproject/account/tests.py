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

    def test_changepassword(self):
        response = self.client.login(username='demo', password='123456')
        self.assertTrue(response)
        data = {
            'oldpass' : '123456',
            'newpass1': '1234567',
            'newpass2': '1234567',
        }
        response = self.client.post('/admin/school/school/add/', data)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/changepassword/')
        self.assertContains(response, "TODO")