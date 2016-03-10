from django.test import TestCase
from apps.requests.models import Request
import datetime


class MiddlewareTest(TestCase):

    def test_middleware(self):
        self.client.get('/')
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Request.objects.count(), 2)


class RequestsModelTest(TestCase):
    def setUp(self):
        for i in range(20, 40):
            Request.objects.create(date=datetime.datetime.now(), method='POST', path='/', server_protocol='HTTP/1.1', ip_addr='31.215.125.%d'%(i), viewed=True)

    def test_requests(self):
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Request.objects.count(), 10)
        self.assertContains(response, '31.215.125.35')
