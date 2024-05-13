from gendiff.module.building_diff import to_str_plain


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
                result += f"Property '{current_path}' was added with value: {to_str_plain(elem['value'])}\n"
            elif elem['status'] == 'deleted':
                result += f"Property '{current_path}' was removed\n"
            elif elem['status'] == 'changed':
                result += f"Property '{current_path}' was updated. From {to_str_plain(elem['old_value'])} to {to_str_plain(elem['new_value'])}\n"  # noqa: E501
        return result
    return walk(collection, '')
