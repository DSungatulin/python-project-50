from gendiff.formatters.format_determinant import get_data_format_plain


def get_plain_view(path, action, old_value, new_value):
    beginning = f"Property '{path}' was"
    if action == 'ADDED':
        comparison_string = f"{beginning} added with value: {get_data_format_plain(new_value)}"
    elif action == 'REMOVED':
        comparison_string = f"{beginning} removed"
    elif action == 'CHANGED':
        comparison_string = (f"{beginning} updated. From {get_data_format_plain(old_value)} to {get_data_format_plain(new_value)}")
    return comparison_string


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
