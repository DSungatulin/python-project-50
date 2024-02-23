from gendiff.formatters.format_determinant import get_data_format


def get_plain_view(path, action, old_value, new_value):
    beginning = f"Property '{path}' was"
    if action == 'ADDED':
        return f"{beginning} added with value: '{get_data_format(new_value)}'"
    if action == 'REMOVED':
        return f"{beginning} removed"
    if action == 'CHANGED':
        return (
            f"{beginning} updated. From '{get_data_format(old_value)}' to '{get_data_format(new_value)}'"
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
