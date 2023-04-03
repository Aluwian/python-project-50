from gendiff.modules.parser import get_file
from gendiff.modules.make_tree import make_tree
from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json_format import get_json_format


def generate_diff(path_1, path_2, name="stylish"):
    data_1 = get_file(path_1)
    data_2 = get_file(path_2)
    result = make_tree(data_1, data_2)
    formatter = get_stylish_format
    if name == "plain":
        formatter = get_plain_format
    if name == "json":
        formatter = get_json_format
    return formatter(result)
