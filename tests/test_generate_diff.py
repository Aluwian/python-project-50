import pytest
from gendiff.generate_diff import generate_diff
from tests.test_helpers import get_fixture_path
from tests.test_helpers import read

plain_result = read(get_fixture_path("fixtures/plain_result.txt"))
nested_result = read(get_fixture_path("fixtures/nested_result.txt"))


@pytest.mark.parametrize(
    "path_1, path_2, expected",
    [
        (
            get_fixture_path("fixtures/file1.json"),
            get_fixture_path("fixtures/file2.json"),
            plain_result,
        ),
        (
            get_fixture_path("fixtures/file1.yml"),
            get_fixture_path("fixtures/file2.yml"),
            plain_result,
        ),
        (
            get_fixture_path("fixtures/file1.json"),
            get_fixture_path("fixtures/file2.yml"),
            plain_result,
        ),
        (
            get_fixture_path("fixtures/nested1.json"),
            get_fixture_path("fixtures/nested2.json"),
            nested_result,
        ),
        (
            get_fixture_path("fixtures/nested1.yaml"),
            get_fixture_path("fixtures/nested2.yaml"),
            nested_result,
        ),
        (
            get_fixture_path("fixtures/nested1.yaml"),
            get_fixture_path("fixtures/nested2.json"),
            nested_result,
        ),
    ],
)
def test_generate_diff(path_1, path_2, expected):
    assert generate_diff(path_1, path_2) == expected
