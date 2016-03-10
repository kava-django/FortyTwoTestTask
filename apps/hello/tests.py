from django.test import TestCase
from apps.hello.models import MyContacts
# Create your tests here.


class MyInfoTest(TestCase):
    fixtures = ['initial_data.json']
    def test_contains(self):
        "tests of contains and status code"
        #self.client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pavlo')
        self.assertContains(response, 'Bredikhin')
        self.assertContains(response, '12 July, 1990')
        self.assertContains(response, 'Become Django Developer')
        self.assertContains(response, 'kava.django@gmail.com')
        self.assertContains(response, 'kava-django@42cc.co')
        self.assertContains(response, 'ng_1990')
        self.assertContains(response, 'https://github.com/kava-django/FortyTwoTestTask/tree/t1_contact')
