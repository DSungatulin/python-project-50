from gendiff.formatters.stylish import get_stylished
from gendiff.formatters.plain import get_plained
from gendiff.formatters.json import json_format


def determine_output_file_format(output_format):
    if output_format == 'stylish':
        return get_stylished
    elif output_format == 'plain':
        return get_plained
    elif output_format == 'json':
        return json_format
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". '
            + 'Available formats are: "stylish", "plain", "json".'
        )
