from improvado.improvado import Dog, ExtractData, Improvado


def main():
    improvado = Improvado()
    extract_data = ExtractData(improvado=improvado)
    extract_data.process_files(
        filenames=[
            '/Users/bryanowsky/Development/improvado/csv_data_1.csv',
            '/Users/bryanowsky/Development/improvado/csv_data_2.csv',
            '/Users/bryanowsky/Development/improvado/json_data.json',
            'other.yaml',
            'clown.png.xlsx'
        ]
    )
    print(extract_data.improvado.data, extract_data.improvado.height)


if __name__ == "__main__":
    main()
