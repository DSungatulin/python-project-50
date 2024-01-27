from gendiff.formatters.format_determinant import get_data_format


# def plain(current_data, property_path=''):
#     lines = []
#     keys_iter = iter(current_data.items())

#     for key, value in keys_iter:
#         current_value1 = get_value_spelling(value)

#         if '  - ' in key and f'  + {key[8:]}' in current_data.keys():
#             key, value = next(keys_iter)
#             current_value2 = get_value_spelling(value)
#             lines.append(
#                 f"""Property '{property_path}{key[6:]}' was updated.
#                 From {current_value1} to {current_value2}"""
#             )

#         elif '  - ' in key:
#             lines.append(f"Property '{property_path}{key[8:]}' was removed")

#         elif '  + ' in key:
#             lines.append(
#                 f"""Property '{property_path}{key[6:]}'
#                 was added with value: {current_value1}"""
#             )

#         elif current_value1 == '[complex value]':
#             new_property_path = property_path + key + '.'
#             lines.append(f'{plain(value, new_property_path)}')

#     return '\n'.join(lines)


def get_plain_view(path, action, old_value, new_value):
    beginning = f"Property '{path}' was "
    if action == 'ADDED':
        return beginning + f'added with value: {get_data_format(new_value)}'
    if action == 'REMOVED':
        return beginning + 'removed'
    if action == 'CHANGED':
        return (
            beginning
            + 'updated. '
            + f'From {get_data_format(old_value)} to {get_data_format(new_value)}'
        )


def get_plained(diff):

    def walk(diff, path, output):
        for entry in diff:
            key = entry['key']
            nested = entry.get('nested')
            if nested:
                walk(nested, path + [key], output)
            else:
                action = entry['action']
                old_value = entry['old value']
                new_value = entry['new value']
                if action == 'UNCHANGED':
                    continue
                output.append(get_plain_view(
                    '.'.join(path + [key]),
                    action,
                    old_value,
                    new_value,
                ))
        return output

    return '\n'.join(walk(diff, [], []))
