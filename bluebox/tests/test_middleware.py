from django.conf import settings
from django.core.urlresolvers import reverse

from django.test import TestCase, Client, modify_settings

from bluebox.tests.testapp.views import TestMiddlewareView


@modify_settings(MIDDLEWARE_CLASSES={
    'append': 'bluebox.middleware.BlueboxMiddleware',
})
class BlueboxMiddlewareTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = '/test-middleware-view/'

    def test_convert_with_middleware(self):
        response = self.client.get(self.url, {'output': 'amp'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response['Content-Type'])
        self.assertEqual(response['touched'], 'True')
        self.assertEqual(response['bbox_converted'], 'True')

    def test_dont_convert_when_no_output_param_in_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['bbox_converted'], 'False')

    def test_dont_convert_when_output_param_not_recognized(self):
        response = self.client.get(self.url, {'output': 'foo'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['bbox_converted'], 'False')

    def test_dont_convert_when_status_code_is_not_200(self):
        response = self.client.get('/foo')
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response['bbox_converted'], 'False')

    def test_dont_convert_when_mimetype_not_html(self):
        response = self.client.get('http://lorem-ipsum.me/api/json')
        self.assertEqual(response['bbox_converted'], 'False')
