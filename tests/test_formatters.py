import json
import pytest
from tests.test_helpers import get_fixture_path
from tests.test_helpers import read
from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json_format import get_json_format
from gendiff.formatters.stylish import stringify


plain_tree = json.load(open(get_fixture_path("fixtures/plain_tree.json")))
nested_tree = json.load(open(get_fixture_path("fixtures/nested_tree.json")))


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            plain_tree,
            read(get_fixture_path("fixtures/plain_result.txt")),
        ),
        (
            nested_tree,
            read(get_fixture_path("fixtures/nested_result.txt")),
        ),
    ],
)
def test_stylish(test_input, expected):
    assert get_stylish_format(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            plain_tree,
            read(get_fixture_path("fixtures/plain_formatter_plain_result.txt")),
        ),
        (
            nested_tree,
            read(
                get_fixture_path("fixtures/plain_formatter_nested_result.txt")
            ),
        ),
    ],
)
def test_plain_format(test_input, expected):
    assert get_plain_format(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            plain_tree,
            read(get_fixture_path("fixtures/json_result_plain.txt")),
        ),
        (
            nested_tree,
            read(get_fixture_path("fixtures/json_result_nested.txt")),
        ),
    ],
)
def test_json_format(test_input, expected):
    assert get_json_format(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            json.load(open(get_fixture_path("fixtures/file1.json"))),
            read(get_fixture_path("fixtures/plain_result_stringify.txt")),
        ),
        (
            {"hello": "world", "is": True, "nested": {"count": 5}},
            read(get_fixture_path("fixtures/nested_stringify.txt")),
        ),
    ],
)
def test_stringify(test_input, expected):
    assert stringify(test_input) == expected
