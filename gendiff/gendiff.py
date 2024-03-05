from gendiff.parser import read_file_data
from gendiff.diff_determinant import get_diff
from gendiff.formatters.output_format_determinant import determine_output_file_format


def generate_diff(filepath1, filepath2, output_format='stylish'):
    config1 = read_file_data(filepath1)
    config2 = read_file_data(filepath2)
    comparison_result = get_diff(config1, config2)
    return determine_output_file_format(comparison_result, output_format)
