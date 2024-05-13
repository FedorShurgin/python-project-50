from gendiff.module.building_diff import print_value


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
