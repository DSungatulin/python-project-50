def get_data_format_stylish(value):
    if isinstance(value, str):
        return value
    elif value is None:
        return 'null'
    return str(value).lower()


def get_data_format_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    return str(value)
