from gendiff.building_diff import building_diff
from gendiff.parser import parse
from gendiff.formatters import format_data


def generate_diff(file1, file2, format='stylish'):
    data = building_diff(parse(file1), parse(file2))
    return format_data(data, format)
