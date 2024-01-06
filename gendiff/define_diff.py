import json


def generate_diff(file_path1, file_path2):
    def generate_diff_recursion(file_content1, file_content2):
        keys = sorted(set(file_content1.keys()) | set(file_content2.keys()))
        diff_lines = []
        for key in keys:
            if key not in file_content2:
                diff_lines.append(f'  - {key}: {file_content1[key]}')
            elif key not in file_content1:
                diff_lines.append(f'  + {key}: {file_content2[key]}')
            elif file_content1[key] != file_content2[key]:
                diff_lines.append(f'  - {key}: {file_content1[key]}')
                diff_lines.append(f'  + {key}: {file_content2[key]}')
            else:
                diff_lines.append(f'    {key}: {file_content1[key]}')
        return '{\n' + '\n'.join(diff_lines) + '\n}'

    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        file_content1 = json.load(f1)
        file_content2 = json.load(f2)
        return generate_diff_recursion(file_content1, file_content2)
