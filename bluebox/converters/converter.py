from bluebox.converters.sanitizer import Sanitizer


class Converter(object):
    output_type = None
    sanitizer = Sanitizer

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

