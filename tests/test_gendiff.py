import pytest

from gendiff.generate_diff import generate_diff, parse

def test_same():
    str1 = {
        "host": "hexlet.io"
    }
    str2 = {
        "host": "hexlet.io"
    } 
    result = '''{
    host: hexlet.io
}''' 
    assert generate_diff(str1,str2) == result


def test_diff():
    str1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
    }
    str2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
    } 
    result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}''' 
    assert generate_diff(str1,str2) == result


def test_parse_json():
  file_json = 'json_file/file1.json'
  result = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
    }
  assert parse(file_json) == result
  
  
def test_parse_yml():
  file_yml = 'json_file/file1.yml'
  result = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
    }
  assert parse(file_yml) == result
