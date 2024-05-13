def to_str_plain(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'  
    return f"'{str(value)}'"


def to_str_stylish(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)


def print_value(value, depth):
    if not isinstance(value, dict):
        return f"{to_str_stylish(value)}\n"
    indent = ' ' * (4 * depth)
    result = '{\n'
    for elem in value:
        result += f"{indent}    {elem}: "
        result += print_value(value[elem], depth+1)
    result += f"{indent}}}\n"
    return result


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
                diff.append(
                    {
                        'key': key,
                        'childrens': building_diff(data1[key], data2[key]),
                        'status': 'nested',
                    }
                )
            else:
                diff.append({'key': key, 'old_value': data1[key], 'new_value': data2[key], 'status': 'changed'})  # noqa: E501
        else:
            diff.append(
                {'key': key, 'value': data2[key], 'status': 'unchanged'}
                )
    return diff
