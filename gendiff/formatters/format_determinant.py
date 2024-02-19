def get_data_format(value):
    if not isinstance(value, dict):
        if value is None:
            data_format = 'null'
        elif isinstance(value, str):
            data_format = f'{str(value)}'
        else:
            data_format = str(value).lower()
    else:
        data_format = '[complex value]'
    return data_format
