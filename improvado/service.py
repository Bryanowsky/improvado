class ImprovadoService:
    def __init__(self, improvado):
        self.improvado = improvado


class ExtractDataService(ImprovadoService):
    def complete_data(self):
        for key in self.improvado.data:
            if len(self.improvado.data[key]) < self.improvado.height:
                self.improvado.data[key].extend([''] * (self.improvado.height - len(self.improvado.data[key])))


class ExportDataService(ImprovadoService):
    def prepare_data(self):
        self.sort_data_by_column()
        output_data = []
        if self.improvado.data:
            headers = list(self.improvado.data.keys())
            output_data.append(headers)
            for index in range(self.improvado.height):
                output_data.append([self.improvado.data[head][index] for head in headers])
        return output_data

    def sort_data_by_column(self, column: str = "D1"):
        if self.improvado.data:
            keys = list(self.improvado.data.keys())
            column = column if self.improvado.data.get(column) else keys[0]
            base = self.improvado.data[column].copy()

            for key in keys:
                self.improvado.data[key] = [
                    x for _, x in sorted(zip(base, self.improvado.data[key]), key=lambda item: item[0])
                ]
