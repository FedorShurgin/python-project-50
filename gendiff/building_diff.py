def building_diff(data1, data2):
    list_keys = data1.keys() | data2.keys()
    sor_list_keys = sorted(list_keys)
    diff = []
    for key in sor_list_keys:
        if key not in data1:
            diff.append(
                {
                    'key': key,
                    'value': data2[key],
                    'status': 'added',
                }
            )
        elif key not in data2:
            diff.append(
                {
                    'key': key,
                    'value': data1[key],
                    'status': 'deleted',
                }
            )
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
                diff.append(
                    {
                        'key': key,
                        'old_value': data1[key],
                        'new_value': data2[key],
                        'status': 'changed',
                    }
                )
        else:
            diff.append(
                {
                    'key': key,
                    'value': data2[key],
                    'status': 'unchanged',
                }
            )
    return diff
