from gendiff.module.building_diff import building_diff
from gendiff.module.to_string import cast_to_a_string
from gendiff.module.to_plain import format_plain
from gendiff.module.to_json import format_json


def generate_diff(file1, file2, format):
    data = building_diff(file1, file2)
    if format == "string":
        return cast_to_a_string(data)
    elif format == "plain":
        return format_plain(data)
    elif format == "json":
        return format_json(data)
    else:
        raise Exception("Incorrect second argument")
