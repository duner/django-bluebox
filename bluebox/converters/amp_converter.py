from bluebox.converters import Converter, Sanitizer


class AMPSanitizer(Sanitizer):
    """
    AMP Blacklist available from:
        https://github.com/ampproject/amphtml/blob/master/spec/amp-html-format.md#html-tags
    """
    blacklisted_attributes = ['style']
    blacklisted_tags = [
        'script',
        'noscript',
        'style',
        'frame',
        'frameset',
        'object',
        'param',
        'applet',
        'form',
        'input',
        'button',
        'textarea',
        'select',
        'option',
        'link',
        'meta'
    ]
    blacklisted_protocols = ['javascript']

    def strip_attributes_extra(self, node):
        for attr in node.attrs.keys():
            if 'on' in attr:
                del node.attrs[attr]


class AMPConverter(Converter):
    output_type = 'amp'
    sanitizer = AMPSanitizer()

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
