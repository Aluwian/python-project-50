import json
import yaml
import os


def parse(file, format_name):
    if format_name == "JSON":
        return json.load(file)
    elif format_name == "YAML":
        return yaml.safe_load(file)


def get_file(path):
    extension = os.path.splitext(path)[1]
    file = open(os.path.abspath(path))
    if extension == ".json":
        return parse(file, "JSON")
    elif extension == ".yml" or ".yaml":
        return parse(file, "YAML")
