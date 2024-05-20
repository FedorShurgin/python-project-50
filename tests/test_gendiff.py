from gendiff.differ import generate_diff
import pytest


@pytest.mark.parametrize(
    'file1,file2,format,expected_result',
    [
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'stylish', 'tests/fixtures/result_stylish.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'plain', 'tests/fixtures/result_plain.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'json', 'tests/fixtures/result_json.txt'),
    ]
)
def test_generate_diff(file1, file2, format, expected_result):
    result = open(expected_result)
    assert generate_diff(file1, file2, format) == result.read()


def test_format():
    file1_json = 'tests/fixtures/file3.json'
    file2_json = 'tests/fixtures/file4.json'
    with pytest.raises(Exception):
        generate_diff(file1_json, file2_json, format='qwery')


def test_expansion():
    file1_json = 'tests/fixtures/file3.json'
    file2_json = 'tests/fixtures/result_stylish.txt'
    with pytest.raises(Exception):
        generate_diff(file1_json, file2_json, format='stylish')
