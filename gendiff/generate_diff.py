import json
import yaml
from pathlib import Path


def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'  
    return f"'{str(value)}'"


def print_value(value, depth):
    if not isinstance(value, dict):
        return f"{to_str(value)}\n"
    indent = ' ' * (4 * depth)
    result = '{\n'
    for elem in value:
        result += f"{indent}    {elem}: "
        result += print_value(value[elem], depth+1)
    result += f"{indent}}}\n"
    return result


def parse(path):
    suffix = Path(path).suffix
    if suffix == ".json":
        return json.load(open(path))
    elif suffix == ".yaml" or suffix == ".yml":
        return yaml.safe_load(open(path))
    else:
        raise Exception("Wrong Extension")


def building_diff(data1, data2):
    list_keys = data1.keys() | data2.keys()
    sor_list_keys = sorted(list_keys)
    diff = []
    for key in sor_list_keys:
        if key not in data1:
            diff.append({'key': key, 'value': data2[key], 'status': 'added'})
        elif key not in data2:
            diff.append({'key': key, 'value': data1[key], 'status': 'deleted'})
        elif data1[key] != data2[key]:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff.append({'key': key, 'childrens': building_diff(data1[key], data2[key]), 'status': 'nested'})  # noqa: E501
            else:
                diff.append({'key': key, 'old_value': data1[key], 'new_value': data2[key], 'status': 'changed'})  # noqa: E501
        else:
            diff.append(
                {'key': key, 'value': data2[key], 'status': 'unchanged'}
                )
    return diff


def cast_to_a_string(collection, depth=0):
    indent = ' ' * (4 * depth)
    result = '{\n'
    for elem in collection:
        if elem['status'] == 'nested':
            result += f"{indent}    {elem['key']}: "
            result += cast_to_a_string(elem['childrens'], depth+1)
        elif elem['status'] == 'added':
            result += f"{indent}  + {elem['key']}: {print_value(elem['value'], depth+1)}"
        elif elem['status'] == 'deleted':
            result += f"{indent}  - {elem['key']}: {print_value(elem['value'], depth+1)}"
        elif elem['status'] == 'changed':
            result += f"{indent}  - {elem['key']}: {print_value(elem['old_value'], depth+1)}"
            result += f"{indent}  + {elem['key']}: {print_value(elem['new_value'], depth+1)}"
        else:
            result += f"{indent}    {elem['key']}: {print_value(elem['value'], depth+1)}"
    result += f"{indent}}}\n"
    return result


def format_plain(collection):

    def walk(node, path):
        result = ''

        if path:
            path += '.'

        for elem in node:
            current_path = path + elem['key']
            if elem['status'] == 'nested':
                result += walk(elem['childrens'], current_path)
            elif elem['status'] == 'added':
                result += f"Property '{current_path}' was added with value: {to_str(elem['value'])}\n"
            elif elem['status'] == 'deleted':
                result += f"Property '{current_path}' was removed\n"
            elif elem['status'] == 'changed':
                result += f"Property '{current_path}' was updated. From {to_str(elem['old_value'])} to {to_str(elem['new_value'])}\n"  # noqa: E501
        return result
    return walk(collection, '')


def format_json(collection):
    return json.dumps(collection)


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
