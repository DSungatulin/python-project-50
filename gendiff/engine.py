def convert_bool_value(val):
    bool_value = {'True': 'true', 'False': 'false'}
    if isinstance(val, bool):
        return bool_value[str(val)]
    else:
        return val
