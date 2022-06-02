import csv
import json
import logging

from os.path import exists
from xml.etree import ElementTree

from improvado.service import ExtractDataService

logging.basicConfig(level=logging.INFO)


class ExtractData:
    def __init__(self, improvado):
        self.improvado = improvado
        self.functions = {
            "csv": self.get_data_from_csv,
            "json": self.get_data_from_json,
            "xml": self.get_data_from_xml
        }

    def process_files(self, filenames: [str]):
        for filename in filenames:
            extension = filename.split('.')[-1]
            self.functions.get(extension, self.unsupported_file)(filename)

    def get_data_from_csv(self, filename):
        if not exists(filename):
            logging.error(f"The file {filename} was not found!")
            return

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    headers = row
                    for head in headers:
                        if self.improvado.data.get(head) is None:
                            self.improvado.data[head] = [''] * self.improvado.height if self.improvado.height else []
                    line_count += 1
                else:
                    for index, item in enumerate(headers):
                        self.improvado.data.get(item).append(str(row[index]))
                    line_count += 1
            self.improvado.height += line_count - 1
        ExtractDataService(improvado=self.improvado).complete_data()
        logging.info(f"Data from {filename} file was successfully extracted!")

    def get_data_from_json(self, filename):
        if not exists(filename):
            logging.error(f"The file {filename} was not found!")
            return

        with open(filename) as json_file:
            data = json.load(json_file)
            rows = data.get("fields", [])

            for row in rows:
                for item in row:
                    if self.improvado.data.get(item):
                        self.improvado.data[item].append(str(row[item]))
                    else:
                        self.improvado.data[row[item]] = [''] * self.improvado.height if self.improvado.height else []

            self.improvado.height += len(rows)
        ExtractDataService(improvado=self.improvado).complete_data()
        logging.info(f"Data from {filename} file was successfully extracted!")

    def get_data_from_xml(self, filename):
        if not exists(filename):
            logging.error(f"The file {filename} was not found!")
            return

        tree = ElementTree.parse(filename)
        root = tree.getroot()

        objects = root[0] if root.__len__() and root[0].tag == "objects" else [0]
        max_values = 0

        for _object in objects:
            if _object.attrib['name']:
                key = _object.attrib['name']
                values = [str(item.text) for item in _object]
                max_values = len(values) if len(values) > max_values else max_values
                if self.improvado.data.get(key):
                    self.improvado.data[key].extend(values)
                else:
                    self.improvado.data[key] = [''] * self.improvado.height if self.improvado.height else []

        self.improvado.height += max_values
        ExtractDataService(improvado=self.improvado).complete_data()
        logging.info(f"Data from {filename} file was successfully extracted!")

    @staticmethod
    def unsupported_file(filename):
        extension = filename.split('.')[-1]
        logging.info(f".{extension} files are not supported yet.")
