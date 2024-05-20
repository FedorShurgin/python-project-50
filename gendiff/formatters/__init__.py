from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_data(data, format):
    if format == "stylish":
        return format_stylish(data)
    elif format == "plain":
        return format_plain(data)
    elif format == "json":
        return format_json(data)
    else:
        raise Exception("Incorrect second argument")
