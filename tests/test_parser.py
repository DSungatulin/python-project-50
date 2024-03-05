from gendiff.parser import read_file_data


def test_read_json_file_data():
    filepath = 'tests/fixtures/flat_files/file1.json'
    expected_data = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    actual_data = read_file_data(filepath)
    assert actual_data == expected_data


def test_read_yaml_file():
    filepath = 'tests/fixtures/flat_files/file2.yml'
    expected_data = {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}
    actual_data = read_file_data(filepath)
    assert actual_data == expected_data


def test_determine_file_format():
    file1 = read_file_data('tests/fixtures/flat_files/file1.json')
    file2 = read_file_data('tests/fixtures/flat_files/file2.yml')
    assert file1 == {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    assert file2 == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}
