from gendiff.building_diff import building_diff
from gendiff.stylish import format_stylish
from gendiff.plain import format_plain
from gendiff.json import format_json


def generate_diff(file1, file2, format):
    data = building_diff(file1, file2)
    if format == "stylish":
        return format_stylish(data)
    elif format == "plain":
        return format_plain(data)
    elif format == "json":
        return format_json(data)
    else:
        raise Exception("Incorrect second argument")
