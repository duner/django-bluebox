from bluebox.converters import Converter
from bluebox.converters.amp.amp_sanitizer import AMPSanitizer

class AMPConverter(Converter):
    output_type = 'amp'
    sanitizer = AMPSanitizer

    def transform(self):
        pass

    def convert(self):
        pass

    def get_canonical_url(self):
        pass

    def get_amp_url(self):
        pass

    def get_amp_css(self):
        pass

    def render_amp_page(self):
        pass

    def convert_html_tags_to_amp(self):
        pass


class AMPVideo(AMPConverter):
    pass


class AMPPost(AMPConverter):
    pass
