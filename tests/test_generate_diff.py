from gendiff.modules.generate_diff import generate_diff
import json

def test_generate_diff():
    path_1 = 'tests/files/file1.json'
    path_2 = 'tests/files/file2.json'
    assert generate_diff(path_1, path_2) == open('tests/fixtures/result_json').read()


print(test_generate_diff())