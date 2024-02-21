from gendiff.parser import determine_file_format
from gendiff.diff_determinant import get_diff
from gendiff.formatters.stylish import get_stylished
from gendiff.formatters.plain import get_plained
from gendiff.formatters.json import json_format


def generate_diff(filepath1, filepath2, output_format='stylish'):
    config1 = determine_file_format(filepath1)
    config2 = determine_file_format(filepath2)

    if output_format == 'stylish':
        apply_format = get_stylished
    elif output_format == 'plain':
        apply_format = get_plained
    elif output_format == 'json':
        apply_format = json_format
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". '
            + 'Available formats are: "stylish", "plain", "json".'
        )

    return apply_format(get_diff(config1, config2)).replace("'","")
