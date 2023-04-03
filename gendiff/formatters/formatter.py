from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json_format import get_json_format


def get_formatter(data, name="stylish"):
    formatter = get_stylish_format
    if name == "plain":
        formatter = get_plain_format
    if name == "json":
        formatter = get_json_format
    return formatter(data)
