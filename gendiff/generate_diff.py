import json
import yaml
from pathlib import Path


def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)


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
                diff.append({'key': key, 'childrens': building_diff(data1[key], data2[key]), 'status': 'nested'})
            else:
                diff.append({'key': key, 'old_value': data1[key], 'new_value': data2[key], 'status': 'changed'})
        else:
            diff.append({'key': key, 'value': data2[key], 'status': 'unchanged'})
    return diff
    
    
def generate_diff(collection, depth):
    indent = ' ' * (4 * depth)
    result = '{\n'
    for elem in collection:
        if elem['status'] == 'nested':
            result += f"{indent}    {elem['key']}: "
            result += generate_diff(elem['childrens'], depth+1)
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
