def get_data_format(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return value
    if value is None:
        return 'null'
    return str(value)
