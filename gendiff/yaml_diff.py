import yaml


def open_yaml(filepath):
    deserialized_file = yaml.safe_load(open(filepath))
    return deserialized_file
