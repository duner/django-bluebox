import six

from django.conf import settings
from bluebox.converters import Converter

"""
TODO:
* Toggle Output Types on and off
* Disable middleware on certain urls
"""


class BlueboxMiddleware(object):

    def can_process_response(self, response):

        print("CODE: " + str(response.status_code))
        
        okay = (response.status_code == 200)
        is_html = ('text/html' in response['Content-Type'])

        if not okay:
            raise ValueError('Bluebox cannot convert responses with failed status codes')
        if not is_html:
            raise ValueError('Bluebox cannot convert non html pages')
        return okay and is_html

    def process_response(self, request, response):
        if not request.GET.get('output', False):
            response.content = 'NOT HERE'
            return response

        if self.can_process_response(response):
            converter = Converter(response.content)
            response.content = "IM HERE"
            # response.content = converter.convert(output=request.OUTPUT_TYPE)
            return response
