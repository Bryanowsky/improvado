import factory
from factory import Factory

from improvado.extract_data import ExtractData
from improvado.improvado import Improvado


class ImprovadoFactory(Factory):

    class Meta:
        model = Improvado


class ExtractDataFactory(Factory):
    improvado = factory.SubFactory(ImprovadoFactory)

    class Meta:
        model = ExtractData
