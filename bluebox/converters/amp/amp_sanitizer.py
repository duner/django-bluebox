from bluebox.converters import Sanitizer

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