from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class FibonacciAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('fib')

    def test_fib_valid(self):
        response = self.client.get(self.url, {'n': 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 55})

    def test_fib_invalid(self):
        # クエリパラメータが存在しない場合
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})

        # クエリパラメータが空文字列の場合
        response = self.client.get(self.url, {'n': ''})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})

        # クエリパラメータが負の数の場合
        response = self.client.get(self.url, {'n': -5})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})

        # クエリパラメータが整数でない場合
        response = self.client.get(self.url, {'n': 'abc'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})

        response = self.client.get(self.url, {'n': '10.5'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})

        # クエリパラメータが非常に大きな数の場合
        response = self.client.get(self.url, {'n': 20000})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})

        # クエリパラメータが特殊文字の場合
        response = self.client.get(self.url, {'n': '!@#'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'status': 400, 'message': 'Bad request.'})