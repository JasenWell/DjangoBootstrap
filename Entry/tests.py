from django.test import TestCase, Client


# Create your tests here.


class MyAppTests(TestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.client = Client(enforce_csrf_checks=False)
    '''
    def test_home(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 302)
    '''
    def test_redirects_after_POST(self):
        response = self.client.post('/login', data={'account': 'hjh','password':'123456'})
        self.assertEqual(response['location'], '/home')
        #self.assertEqual(response['location'], '/')
        self.assertEqual(response.status_code, 302)
