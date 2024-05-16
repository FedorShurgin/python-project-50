def to_str(value, depth):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        indent = ' ' * (4 * depth)
        result = '{\n'
        for elem in value:
            result += f"{indent}    {elem}: "
            result += to_str(value[elem], depth+1) + '\n'
        result += f"{indent}}}"
        return result
    else:
        return str(value)


def format_stylish(collection, depth=0):
    indent = ' ' * (4 * depth)
    result = '{\n'
    for elem in collection:
        if elem['status'] == 'nested':
            result += f"{indent}    {elem['key']}: "
            result += format_stylish(elem['childrens'], depth+1)
        elif elem['status'] == 'added':
            result += f"{indent}  + {elem['key']}: {to_str(elem['value'], depth+1)}\n"  # noqa: E501
        elif elem['status'] == 'deleted':
            result += f"{indent}  - {elem['key']}: {to_str(elem['value'], depth+1)}\n"  # noqa: E501
        elif elem['status'] == 'changed':
            result += f"{indent}  - {elem['key']}: {to_str(elem['old_value'], depth+1)}\n"  # noqa: E501
            result += f"{indent}  + {elem['key']}: {to_str(elem['new_value'], depth+1)}\n"  # noqa: E501
        else:
            result += f"{indent}    {elem['key']}: {to_str(elem['value'], depth+1)}\n"  # noqa: E501
    result += f"{indent}}}\n"
    return result
