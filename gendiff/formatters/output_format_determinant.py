from gendiff.formatters.stylish import get_stylished
from gendiff.formatters.plain import get_plained
from gendiff.formatters.json import get_jsoned


def determine_output_file_format(diff, output_format):
    if output_format == 'stylish':
        return get_stylished(diff)
    elif output_format == 'plain':
        return get_plained(diff)
    elif output_format == 'json':
        return get_jsoned(diff)
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". '
            + 'Available formats are: "stylish", "plain", "json".'
        )
