def make_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = []
    for key in keys:
        if key not in data1:
            result.append({'name': key, 'type': "added", 'value': data2[key]})
        elif key not in data2:
            result.append({'name': key, 'type': "deleted", 'value': data1[key]})
        elif data1[key] == data2[key]:
            result.append({'name': key, 'type': "no-change",
                           'value': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({'name': key, 'type': "parent",
                           'children': make_tree(data1[key], data2[key])})
        else:
            result.append({'name': key, 'type': "update",
                           'value_1': data1[key], 'value_2': data2[key]})
    return result
