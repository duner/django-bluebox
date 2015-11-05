from bs4 import BeautifulSoup

class Converter(object):
    output_type = None
    sanitizer = None

    def __init__(self, content, output=None):
        self.content = content
        if output:
            self.output = output
            return self.factory(output)

    @staticmethod
    def factory(self):
        output_types = {}
        subclasses = self.__subclasses__()
        for subclass in subclasses:
            output_types[subclass.output_type] = subclass
        if self.output not in output_types.keys():
            raise KeyError("{} is not a valid output type").format(self.output)
        return output_types[self.output]

    @classmethod
    def get_output_types(self):
        types = []
        for subclass in self.__subclasses__():
            types.append(subclass.output_type)
        return types

    def convert(self):
        stripped = self.sanitizer(self.content).strip()
        return stripped


class Sanitizer(object):
    blacklisted_tags = []
    blacklisted_attributes = []
    blacklisted_protocols = []

    def __init__(self, tags=None, attributes=None, protocols=None):
        if tags:
            self.blacklisted_tags = tags
        if attributes:
            self.blacklisted_attributes = attributes
        if protocols:
            self.blacklisted_protocols = protocols

    def strip(self, content=None):
        """Strip HTML content to meet standards of output type.
        Meant to be subclassed for each converter.

        Keyword arguments:
        content -- subset of an HTML document. (ie. contents of a body tag)
        """
        if not content:
            content = self.content
            return content

        soup = BeautifulSoup(content, "lxml")
        self.strip_tags(soup)
        self.strip_attributes(soup)

        output = soup.body.decode_contents()
        return output

    def strip_tags(self, soup):
        if self.blacklisted_tags:
            [x.extract() for x in soup.find_all(self.blacklisted_tags)]

    def strip_attributes_extra(self, node):
        pass

    def strip_attributes(self, soup):
        if not (self.blacklisted_attributes or self.blacklisted_protocols):
            return

        for node in soup.body.find_all(True):
            attributes = node.attrs.keys()
            if not attributes:
                continue

            for attr in self.blacklisted_attributes:
                if attr in attributes:
                    del node.attrs[attr]

            self.strip_attributes_extra(node)

            if 'href' in attributes:
                protocol = node['href'].split(':')[0]
                if protocol in self.blacklisted_protocols:
                    del node['href']
