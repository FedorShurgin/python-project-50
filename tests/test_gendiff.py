from gendiff.generate_diff import generate_diff
import pytest


def test_gendiff():
    file1_json = 'tests/fixtures/file3.json'
    file2_json = 'tests/fixtures/file4.json'
    result_stylish = open('tests/fixtures/result_stylish.txt')
    result_plain = open('tests/fixtures/result_plain.txt')
    result_json = open('tests/fixtures/result_json.txt')
    assert generate_diff(file1_json, file2_json, format='stylish') == result_stylish.read()
    assert generate_diff(file1_json, file2_json, format='plain') == result_plain.read()
    assert generate_diff(file1_json, file2_json, format='json') == result_json.read()
    result_stylish.close()
    result_plain.close()
    result_json.close()


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


'''
тест на ошибочное расширение(txt)
тест на ошибочный форматор(wrong format)
'''