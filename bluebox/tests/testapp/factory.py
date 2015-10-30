import factory

from .models import *

class MockObjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MockObject

    content = """
    <p>Hello how are you doing</p>
    <img src="http://bukk.it/l2internet2.gif" />
    """