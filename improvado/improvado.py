import logging


from improvado.export_data import ExportData
from improvado.extract_data import ExtractData

logging.basicConfig(level=logging.INFO)


class Improvado:
    def __init__(self):
        self.data = {}
        self.height = 0

    def extract_data(self, filenames: [str]):
        extract = ExtractData(improvado=self)
        extract.process_files(filenames=filenames)

    def export_data(self, filename: str = "output.tsv"):
        export = ExportData(improvado=self)
        export.export_data(filename=filename)
