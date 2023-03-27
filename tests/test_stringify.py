from gendiff.modules.stylish import stringify
import os
import json


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_stringify_plant():
    text = json.load(open(get_fixture_path('fixtures/file1.json')))
    result = read(get_fixture_path('fixtures/plain_result_stringify.txt'))
    assert stringify(text, 0) == result


def test_stringify_nested():
    data = {"hello": "world", "is": True, "nested": {"count": 5}}
    result = read(get_fixture_path('fixtures/nested_stringify.txt'))
    assert stringify(data) == result
