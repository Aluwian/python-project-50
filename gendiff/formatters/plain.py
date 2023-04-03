def get_plain_format(data):
    return "\n".join(filter(lambda x: x is not None, make_plain(data)))


def make_plain(tree, parent_name=""):
    result = []
    for item in tree:
        key = item.get("name")
        if parent_name != "":
            key = f"{parent_name}.{key}"
        children = item.get("children")
        if children:
            result.extend(make_plain(children, key))
        result.append(format_changes(item, key))
    return result


def format_changes(dictionary, key):
    value = format_value(dictionary.get("value"))
    value_1 = format_value(dictionary.get("value_1"))
    value_2 = format_value(dictionary.get("value_2"))
    object_type = dictionary.get("type")
    if object_type == "deleted":
        return f"Property '{key}' was removed"
    elif object_type == "added":
        return f"Property '{key}' was added with value: {value}"
    elif object_type == "update":
        return f"Property '{key}' was updated. From {value_1} to {value_2}"


def format_value(value):
    if type(value) is bool:
        return (str(value)).lower()
    if type(value) is dict:
        return "[complex value]"
    if value is None:
        return "null"
    if type(value) == str:
        return f"'{value}'"
    return str(value)
