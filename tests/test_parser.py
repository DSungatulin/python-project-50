import pytest
from gendiff.parser import determine_file_format


def test_determine_file_format():
    file1 = determine_file_format('tests/fixtures/flat_files/file1.json')
    file2 = determine_file_format('tests/fixtures/flat_files/file2.yml')
    assert file1 == {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}
    assert file2 == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}

def test_determine_file_format_invalid():
    with pytest.raises(TypeError) as excinfo:
        determine_file_format('tests/fixtures/comparison_results/correct_flat_comparison.txt')
    assert 'Invalid file format!' in str(excinfo.value)
