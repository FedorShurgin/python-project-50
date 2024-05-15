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
                result += f"Property '{current_path}' was added with value: {to_str_plain(elem['value'])}\n"  # noqa: E501
            elif elem['status'] == 'deleted':
                result += f"Property '{current_path}' was removed\n"
            elif elem['status'] == 'changed':
                result += f"Property '{current_path}' was updated. From {to_str_plain(elem['old_value'])} to {to_str_plain(elem['new_value'])}\n"  # noqa: E501
        return result
    return walk(collection, '')
