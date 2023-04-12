from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json_format import get_json_format


def get_formatter(name):
    match name:
        case "stylish":
            return get_stylish_format
        case "plain":
            return get_plain_format
        case "json":
            return get_json_format
        case _:
            raise ValueError(
                f"Unknown format {name}. "
                f"Use supported formats: stylish, plant, json"
            )
