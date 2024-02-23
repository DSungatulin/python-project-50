def get_data_format_stylish(value):
    if isinstance(value, str):
        data_format = value
    elif value is None:
        data_format = 'null'
    else:
        data_format = str(value).lower()
    return data_format


def get_data_format_plain(value):
    if isinstance(value, dict):
        data_format = '[complex value]'
    elif isinstance(value, bool):
        data_format = str(value).lower()
    elif isinstance(value, str):
        data_format = f"'{value}'"
    elif value is None:
        data_format = 'null'
    else:
        data_format = str(value)
    return data_format
