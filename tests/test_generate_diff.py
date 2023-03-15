from gendiff.modules.generate_diff import generate_diff


def test_json():
    path_1 = 'tests/fixtures/files/file1.json'
    path_2 = 'tests/fixtures/files/file2.json'
    assert generate_diff(path_1, path_2) == open('tests/fixtures/results/result_json').read()


def test_yaml():
    path_1 = 'tests/fixtures/files/file1.yml'
    path_2 = 'tests/fixtures/files/file2.yml'
    right_answer = open('tests/fixtures/results/result_yml').read()
    assert generate_diff(path_1, path_2) == right_answer
