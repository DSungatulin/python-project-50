from gendiff.formatters.format_determinant import get_data_format


# def stylish(  # noqa: C901
#     current_data, depth=0, spaces_number=4, leftward_shift=2
# ):
#     replacer = ' '
#     lines = []

#     if not isinstance(current_data, dict):
#         if current_data is None:
#             return 'null'
#         if isinstance(current_data, str):
#             return current_data.lower()
#         return str(current_data).lower()

#     indent_deep_size = depth + spaces_number
#     current_indent = replacer * depth
#     for key, value in current_data.items():
#         if '  - ' in key:
#             indent_depth = replacer * (indent_deep_size - leftward_shift)
#             key_output = f'- {key[8:]}'
#         elif '  + ' in key:
#             indent_depth = replacer * (indent_deep_size - leftward_shift)
#             key_output = f'+ {key[6:]}'
#         else:
#             indent_depth = replacer * indent_deep_size
#             key_output = key
#         lines.append(
#             f'{indent_depth}{key_output}: {stylish(value, indent_deep_size)}'
#         )
#     result = itertools.chain("{", lines, [current_indent + "}"])
#     return '{\n' + '\n'.join(result) + '\n}'


# def format_stylish(diff):
#     def inner_format(diff, depth=1):
#         result = []
#         indent = '  ' * depth
#         for key, value in diff.items():
#             if value == 'nested_diff':
#                 result.append(f'{indent}  {key}: {{\n{inner_format(diff[key], depth+1)}\n{indent}  }}')
#             elif value is None:
#                 result.append(f'{indent}  {key}: null')
#             elif isinstance(value, dict):
#                 result.append(f'{indent}  {key}: {{\n{inner_format(value, depth+1)}\n{indent}  }}')
#             else:
#                 result.append(f'{indent}  {key}: {value}')
#         return '\n'.join(result)

#     return '{\n' + inner_format(diff) + '\n}'


INDENT_CHAR = ' '
INDENT_NUMBER = 4
LEFTWARD_SHIFT = 2


def get_stylish_view(key, value, special_char, depth, indent):

    def walk(dict_, output, depth, indent):
        for key, value in dict_.items():
            beginning = f'{INDENT_CHAR * INDENT_NUMBER * depth + key}: '
            if isinstance(value, dict):
                output.append(
                    beginning
                    + walk(value, [], depth + 1, indent + INDENT_CHAR * INDENT_NUMBER)
                )
            else:
                output.append(beginning + get_data_format(value))
        return (
            '{\n' + '\n'.join(output)
            + f'\n{indent + INDENT_CHAR[0:LEFTWARD_SHIFT]}' + '}'
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
        indent = (INDENT_CHAR * INDENT_NUMBER * depth)[0:LEFTWARD_SHIFT]
        for entry in diff:
            key = entry['key']
            nested = entry.get('nested')
            special_char = '  '
            if nested:
                output.append(indent + special_char + key + ': {')
                walk(nested, output, depth + 1)
                output.append(indent + INDENT_CHAR[0:LEFTWARD_SHIFT] + '}')
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
