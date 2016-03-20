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


class ContainsEditTest(TestCase):
    fixtures = ['initial_data.json']

    def test_contains_edit(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'edit')
        self.assertContains(response, 'login')

    def test_login(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_edit_info_valid(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/edit/1/')
        edit_data = {'name': 'Test1',
                     'surname': 'Test2',
                     'date_of_birth': '1990-01-01',
                     'bio': 'Test3',
                     'email': 'test4@test.tst',
                     'jabber': 'test5@test.tst',
                     'skype': 'test6',
                     'other_contacts': 'test7',
                     'photo': ''}
        edit = self.client.post('/edit/1/', edit_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(edit.status_code, 200)
        response = self.client.get('/')
        self.assertContains(response, 'Test1')

    def test_edit_info_invalid(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/edit/1/')
        edit_data = {'name': 'Test1',
                     'surname': 'Test2',
                     'date_of_birth': '1990-01-01',
                     'bio': 'Test3',
                     'email': 'test4@test',
                     'jabber': 'test5@test.tst',
                     'skype': 'test6',
                     'other_contacts': 'test7',
                     'photo': ''}
        edit = self.client.post('/edit/1/', edit_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(edit.status_code, 400)

