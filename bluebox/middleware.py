
from django.conf import settings
from bluebox.converters import Converter

"""
TODO:
* Toggle Output Types on and off
* Disable middleware on certain urls
"""


class BlueboxMiddleware(object):

    def can_process_response(self, response):
        okay = (response.status_code == 200)
        is_html = ('text/html' in response['Content-Type'])
        return okay and is_html

    def process_response(self, request, response):
        if not request.GET.get('output', False):
            response['bbox_converted'] = False
            return response

        if self.can_process_response(response):
            converter = Converter(response.content)
            response['touched'] = True
            response['bbox_converted'] = True
            # response.content = converter.convert(output=request.OUTPUT_TYPE)
            return response
