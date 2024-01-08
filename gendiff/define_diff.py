from gendiff.parser import determine_file_format


def generate_diff(filepath1, filepath2):
    def generate_diff_recursion(first_file_content, second_file_content):
        keys = sorted(set(first_file_content.keys()) | set(second_file_content.keys()))
        diff_lines = []
        for key in keys:
            if key not in second_file_content:
                diff_lines.append(f'  - {key}: {first_file_content[key]}')
            elif key not in first_file_content:
                diff_lines.append(f'  + {key}: {second_file_content[key]}')
            elif first_file_content[key] != second_file_content[key]:
                diff_lines.append(f'  - {key}: {first_file_content[key]}')
                diff_lines.append(f'  + {key}: {second_file_content[key]}')
            else:
                diff_lines.append(f'    {key}: {first_file_content[key]}')
        return '{\n' + '\n'.join(diff_lines) + '\n}'

    with open(filepath1, 'r') as f1, open(filepath2, 'r') as f2:
        data1 = determine_file_format(f1)
        data2 = determine_file_format(f2)
        return generate_diff_recursion(data1, data2)
