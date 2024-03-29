from gendiff.parser import get_file
from gendiff.make_tree import make_tree
from gendiff.formatters.formatter import get_formatter


def generate_diff(path_1, path_2, name="stylish"):
    data_1 = get_file(path_1)
    data_2 = get_file(path_2)
    result = make_tree(data_1, data_2)
    formatter = get_formatter(name)
    return formatter(result)
