from django.test import TestCase
from django.test.client import Client

class UserFunctionTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_creatingflashcard(self):
        response = self.client.login(username='demo', password='123456')
        self.assertTrue(response)
        data = {
            'title' : 'test',
            'description':'test creating flashcard',
            'grade' : 'first',
            'subject' : 'art',
            'Prompt 01':'test01',
            'Answer 01' : 'answer01',
            'Prompt 02':'test',
            'Answer 02' : 'answer01'
        }
        response = self.client.post('/create/', data)
        self.assertEqual(response.status_code, 200)