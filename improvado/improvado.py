import csv
import json


class Improvado:
    def __init__(self):
        self.data = {}
        self.height = 0


class ExtractData:
    def __init__(self, improvado: Improvado):
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
                        self.improvado.data.get(item).append(row[index])
                    line_count += 1
            self.improvado.height += line_count - 1

    def get_data_from_json(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            rows = data.get("fields", [])
            for row in rows:
                print(row)

    def get_data_from_xml(self, filename):
        print("This is a xml", filename)

    @staticmethod
    def unsupported_file(filename):
        extension = filename.split('.')[-1]
        print(f".{extension} files are not supported yet.")

