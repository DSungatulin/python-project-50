from gendiff.formatters.format_determinant import get_data_format


INDENT_CHAR = ' '
INDENT_NUMBER = 4
LEFTWARD_SHIFT = 2


def get_stylish_view(key, value, special_char, depth, indent):

    def walk(dict_, output, depth, indent):
        for key, value in dict_.items():
            beginning = f'{INDENT_CHAR * INDENT_NUMBER * depth + key}: '
            if isinstance(value, dict):
                output.append(
                    beginning + walk(value, [], depth + 1, indent + INDENT_CHAR * INDENT_NUMBER)  # noqa: E501
                )
            else:
                output.append(beginning + get_data_format(value))
        return (
            '{\n' + '\n'.join(output)
            + f'\n{indent + INDENT_CHAR[0:-LEFTWARD_SHIFT]}' + '}'
        )

    if isinstance(value, dict):
        formatted = walk(value, [], depth + 1, indent)
    else:
        formatted = get_data_format(value)

    return f'{indent + special_char + key}: {formatted}'


def form_string(key, action, old_value, new_value, depth, indent):
    if action == 'ADDED':
        return get_stylish_view(key, new_value, '+ ', depth, indent)
    if action == 'REMOVED':
        return get_stylish_view(key, old_value, '- ', depth, indent)
    if action == 'CHANGED':
        return '\n'.join((
            get_stylish_view(key, old_value, '- ', depth, indent),
            get_stylish_view(key, new_value, '+ ', depth, indent),
        ))
    if action == 'UNCHANGED':
        return get_stylish_view(key, old_value, '  ', depth, indent)


def get_stylished(diff):

    def walk(diff, output, depth):
        indent = (INDENT_CHAR * INDENT_NUMBER * depth)[0:-LEFTWARD_SHIFT]
        for entry in diff:
            key = entry['key']
            nested = entry.get('nested')
            special_char = '  '
            if nested:
                output.append(indent + special_char + key + ': {')
                walk(nested, output, depth + 1)
                output.append(indent + INDENT_CHAR * INDENT_NUMBER[0:-LEFTWARD_SHIFT] + '}')
            else:
                action = entry['action']
                old_value = entry['old value']
                new_value = entry['new value']
                output.append(form_string(
                    key,
                    action,
                    old_value,
                    new_value,
                    depth,
                    indent,
                ))
        return output

    return '{\n' + '\n'.join(walk(diff, [], 1)) + '\n}'
