class TestExtractData:
    def test_extract_data_with_unsupported_files(self, caplog, unsupported_files, extract_data):
        expected_records = [
            ".yml files are not supported yet.",
            ".xlsx files are not supported yet."
        ]
        extract_data.process_files(filenames=unsupported_files)

        assert {} == extract_data.improvado.data
        assert 2 == len(caplog.records)
        assert expected_records == [record.msg for record in caplog.records]
