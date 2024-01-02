import json


def generate_diff(file_path1, file_path2):
    def generate_diff_recursion(data1, data2):
        keys = sorted(set(data1.keys()) | set(data2.keys()))
        diff_lines = []
        for key in keys:
            if key not in data2:
                diff_lines.append(f'  - {key}: {data1[key]}')
            elif key not in data1:
                diff_lines.append(f'  + {key}: {data2[key]}')
            elif data1[key] != data2[key]:
                diff_lines.append(f'  - {key}: {data1[key]}')
                diff_lines.append(f'  + {key}: {data2[key]}')
            else:
                diff_lines.append(f'    {key}: {data1[key]}')
        return '{\n' + '\n'.join(diff_lines) + '\n}'

    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
        return generate_diff_recursion(data1, data2)
