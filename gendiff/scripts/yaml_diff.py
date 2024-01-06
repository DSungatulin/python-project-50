import yaml


def open_yaml(file_path):
    deserialized_file = yaml.safe_load(open(file_path))
    return deserialized_file
