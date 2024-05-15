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


def format_stylish(collection, depth=0):
    indent = ' ' * (4 * depth)
    result = '{\n'
    for elem in collection:
        if elem['status'] == 'nested':
            result += f"{indent}    {elem['key']}: "
            result += format_stylish(elem['childrens'], depth+1)
        elif elem['status'] == 'added':
            result += f"{indent}  + {elem['key']}: {print_value(elem['value'], depth+1)}"  # noqa: E501
        elif elem['status'] == 'deleted':
            result += f"{indent}  - {elem['key']}: {print_value(elem['value'], depth+1)}"  # noqa: E501
        elif elem['status'] == 'changed':
            result += f"{indent}  - {elem['key']}: {print_value(elem['old_value'], depth+1)}"  # noqa: E501
            result += f"{indent}  + {elem['key']}: {print_value(elem['new_value'], depth+1)}"  # noqa: E501
        else:
            result += f"{indent}    {elem['key']}: {print_value(elem['value'], depth+1)}"  # noqa: E501
    result += f"{indent}}}\n"
    return result
