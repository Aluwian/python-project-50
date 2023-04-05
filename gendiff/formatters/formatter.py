from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json_format import get_json_format


def get_formatter(name):
    if name == "plain":
        return get_plain_format
    if name == "json":
        return get_json_format
    return get_stylish_format
