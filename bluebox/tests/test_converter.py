from django.test import TestCase
from bluebox.converters import Sanitizer


class BlueboxSanitizerTestCase(TestCase):

    def test_strip_tags(self):
        test_html = ('<div><p>HelloWorld<b>boldtext</b></p>'
                     '<img src="http://bukk.it/l2internet2.gif" /></div>')
        expected_output = "<div><p>HelloWorld</p></div>"
        sanitizer = Sanitizer(tags=['img', 'b'])
        self.assertEqual(expected_output, sanitizer.strip(content=test_html))

    def test_remove_blacklisted_protocols(self):
        test_html = '<a href="javascript:;"></a>'
        expected_output = "<a></a>"
        sanitizer = Sanitizer(protocols=['javascript'])
        self.assertEqual(expected_output, sanitizer.strip(content=test_html))

    def test_dont_remove_nonblacklisted_protocols(self):
        test_html = '<a href="http://google.com"></a>'
        sanitizer = Sanitizer(protocols=['javascript'])
        self.assertEqual(test_html, sanitizer.strip(content=test_html))

    def test_remove_blacklisted_attributes(self):
        test_html = '<div style="color: papayawhip;" width="100%"></div>'
        expected_output = '<div width="100%"></div>'
        sanitizer = Sanitizer(attributes=['style'])
        self.assertEqual(expected_output, sanitizer.strip(content=test_html))
