def get_action(dict1_key, dict2_key, old_value, new_value):
    if dict2_key and not dict1_key:
        return 'ADDED'
    if dict1_key and not dict2_key:
        return 'REMOVED'
    if old_value != new_value:
        return 'CHANGED'
    return 'UNCHANGED'


def get_diff(dict1, dict2):
    diff = []
    keys = sorted(list(set(dict1) | set(dict2)))

    for key in keys:
        old_value = dict1.get(key)
        new_value = dict2.get(key)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            diff.append({'key': key, 'nested': get_diff(old_value, new_value)})
        else:
            diff.append({
                'key': key,
                'action': get_action(
                    key in dict1,
                    key in dict2,
                    old_value,
                    new_value,
                ),
                'old value': old_value,
                'new value': new_value,
            })

    return diff
