import pytest

from gendiff.generate_diff import generate_diff, parse


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
