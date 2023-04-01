import os
import json
from gendiff.formatters.plain import get_plain_format


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, file_name)


def read(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def test_plain_format():
    tree = json.load(open(get_fixture_path("fixtures/plain_tree.json")))
    result = read(get_fixture_path("fixtures/plain_formatter_plain_result.txt"))
    assert get_plain_format(tree) == result


def test_nested_format():
    tree = json.load(open(get_fixture_path("fixtures/nested_tree.json")))
    result = read(
        get_fixture_path("fixtures/plain_formatter_nested_result.txt")
    )
    assert get_plain_format(tree) == result
