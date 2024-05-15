from gendiff.building_diff import building_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.parser import parse


def to_format(data, format):
    if format == "stylish":
        return format_stylish(data)
    elif format == "plain":
        return format_plain(data)
    elif format == "json":
        return format_json(data)
    else:
        raise Exception("Incorrect second argument")


def generate_diff(file1, file2, format):
    data = building_diff(parse(file1), parse(file2))
    return to_format(data, format)
