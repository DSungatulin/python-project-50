# from gendiff.parser import determine_file_format


# def generate_diff(filepath1, filepath2, format='stylish'):
    
#     file1_content = determine_file_format(filepath1)
#     file2_content = determine_file_format(filepath2)
    
#     if isinstance(file1_content, str) or isinstance(file2_content, str):
#         return 'File content is not in dictionary format'
    
#     keys = sorted(set(file1_content.keys()) | set(file2_content.keys()))
#     diff_lines = []
    
#     for key in keys:
#         if key not in file2_content:
#             diff_lines.append(f'  - {key}: {file1_content[key]}')
#         elif key not in file1_content:
#             diff_lines.append(f'  + {key}: {file2_content[key]}')
#         elif file1_content[key] != file2_content[key]:
#             diff_lines.append(f'  - {key}: {file1_content[key]}')
#             diff_lines.append(f'  + {key}: {file2_content[key]}')
#         else:
#             diff_lines.append(f'    {key}: {file1_content[key]}')
#     return '{\n' + '\n'.join(diff_lines) + '\n}'


def get_action(key_in_dict1, key_in_dict2, old_value, new_value):
    if key_in_dict2 and not key_in_dict1:
        return 'ADDED'
    if key_in_dict1 and not key_in_dict2:
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
