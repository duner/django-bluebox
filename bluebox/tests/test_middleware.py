import requests

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase, Client, modify_settings
from bluebox.tests.testapp.views import TestMiddlewareView

from bluebox.converters import Converter, Sanitizer
from bluebox.converters.amp import AMPConverter
from bluebox.converters import amp as amptest

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
        response = requests.get('https://api.github.com/users/duner')
        self.assertNotIn('text/html', response.headers['content-type'])
