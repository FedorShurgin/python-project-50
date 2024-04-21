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
    
    
def generate_diff(data1, data2):
    list_keys = data1.keys() | data2.keys()
    sor_list_keys = sorted(list_keys)
    result = '{\n'
    for key in sor_list_keys:
        if key not in data1:
            result += f'  + {key}: {to_str(data2[key])}\n'
        elif key not in data2:
            result += f'  - {key}: {to_str(data1[key])}\n'
        elif data1[key] != data2[key]:
            result += f'  - {key}: {to_str(data1[key])}\n  + {key}: {to_str(data2[key])}\n'
        else:
            result += f'    {key}: {to_str(data2[key])}\n'
    result += '}'
    return result
