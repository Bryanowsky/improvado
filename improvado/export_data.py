import csv
import logging

from improvado.service import ExportDataService
from improvado.utils import generate_unique_filename

logging.basicConfig(level=logging.INFO)


class ExportData:
    def __init__(self, improvado):
        self.improvado = improvado
        self.functions = {
            "tsv": self.export_data_as_tsv
        }

    def export_data(self, filename: str = "output.tsv"):
        if not self.improvado.data:
            logging.error(f"No data detected!")
            return

        extension = filename.split('.')[-1]
        self.functions.get(extension, self.unsupported_file)(filename)

    def export_data_as_tsv(self, filename: str):
        filename = generate_unique_filename(filename=filename)
        with open(filename, 'w') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            for line in ExportDataService(improvado=self.improvado).prepare_data():
                writer.writerow(line)
        tsvfile.close()
        logging.info(f"The file {filename} was generated successfully!")

    @staticmethod
    def unsupported_file(filename: str):
        extension = filename.split('.')[-1]
        print(f".{extension} as output file is not supported yet.")
