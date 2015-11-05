from django.conf import settings
from bluebox.converters import Converter

"""
TODO:
* Toggle Output Types on and off
* Disable middleware on certain urls
"""


class BlueboxMiddleware(object):

    def can_process_response(self, request, response):
        okay = (response.status_code == 200)
        is_html = ('text/html' in response['Content-Type'])
        valid_output_type = (request.GET.get('output', False) in Converter.get_output_types())
        return (okay and is_html and valid_output_type)

    def process_response(self, request, response):
        if self.can_process_response(request, response):
            converter = Converter(response.content)
            response['bbox_converted'] = True
            # response.content = converter.convert(output=request.OUTPUT_TYPE)
            return response
        else:
            response['bbox_converted'] = False
            return response
