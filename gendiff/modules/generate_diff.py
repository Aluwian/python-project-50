from gendiff.modules.parser import get_file
from gendiff.modules.make_tree import make_tree
from gendiff.modules.stylish import get_format


def generate_diff(path_1, path_2, formatter=get_format):
    data_1 = get_file(path_1)
    data_2 = get_file(path_2)
    result = make_tree(data_1, data_2)
    return formatter(result)
