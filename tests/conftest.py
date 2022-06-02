import pytest

from improvado.factories import ExtractDataFactory, ImprovadoFactory


@pytest.fixture
def empty_improvado():
    improvado = ImprovadoFactory.create()
    return improvado


@pytest.fixture
def extract_data():
    improvado = ExtractDataFactory.create()
    return improvado


@pytest.fixture
def unsupported_files():
    filenames = ["file.yml", "file.xlsx"]
    return filenames
