from django.conf import settings
from django.test import TestCase
from django.test import Client
from django.test.utils import override_settings

from bluebox.tests.testapp.factory import MockObjectFactory
from bluebox.tests.testapp.models import MockObject


MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES += ('bluebox.middleware.BlueboxMiddleware', )


@override_settings(MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES)
class BlueboxMiddlewareTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.object = MockObjectFactory()
        self.url = self.object.get_absolute_url()
        print(MockObject.objects.all())
        print("URL: " + self.url)

    def test_convert_with_middleware(self):
        response = self.client.get(self.url + '/?output=amp')
        self.assertEqual(response.content, b'IM HERE')

    # def test_dont_convert_when_no_output_param_in_url(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.content, b'NOT HERE')

    # def test_dont_convert_when_output_param_not_recognized(self):
    #     response = self.client.get(self.url + '/?output=foo')
    #     self.assertEqual(response.content, b'NOT HERE')

    # def test_dont_convert_when_status_code_is_not_200(self):
    #     response = self.client.get('/foo')
    #     self.assertRaises(ValueError)

    def test_dont_convert_when_mimetype_not_html(self):
        pass
