# from bluebox.converters import AMPConverter

class Converter(object):
    output_type = None

    def __init__(self, content=None, output=None):
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
        pass