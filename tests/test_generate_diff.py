from gendiff.modules.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


plain_answer = read(get_fixture_path('plain_result.txt'))
nested_answer = read(get_fixture_path('nested_result.txt'))


def test_plain_json():
    path_1 = get_fixture_path('file1.json')
    path_2 = get_fixture_path('file2.json')
    assert generate_diff(path_1, path_2) == plain_answer


def test_plain_yaml():
    path_1 = get_fixture_path('file1.yml')
    path_2 = get_fixture_path('file2.yml')
    assert generate_diff(path_1, path_2) == plain_answer


def test_nested_json():
    path1 = get_fixture_path('nested1.json')
    path2 = get_fixture_path('nested2.json')
    assert generate_diff(path1, path2) == nested_answer


def test_nested_yml():
    path1 = get_fixture_path('nested1.yaml')
    path2 = get_fixture_path('nested2.yaml')
    assert generate_diff(path1, path2) == nested_answer

