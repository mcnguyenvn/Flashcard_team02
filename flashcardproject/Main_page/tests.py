from django.test import TestCase
from django.test.client import Client

class UserFunctionTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.post('/login/', {'username': 'demo', 'password': '123456'})
        self.assertEqual(response.status_code, 302)

    def test_failed_login(self):
        # Wrong username and password
        response = self.client.post('/login/', {'username': 'wrong_username', 'password': ''})
        self.assertContains(response, "TODO .", status_code=200)

    def test_logout(self):
        response = self.client.login(username='demo', password='123456')
        self.assertTrue(response)
        response = self.client.logout()
        self.assertEqual(response, None)
        response = self.client.post('/logout/')
        self.assertContains(response, "TODO .")