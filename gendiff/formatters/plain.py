def get_plain_format(data):
    return "\n".join(make_plain(data))


def make_plain(tree, parent_name=""):
    result = []
    for item in tree:
        key = item.get("name")
        if parent_name != "":
            key = f"{parent_name}.{key}"
        value = format_value(item.get("value"))
        value_1 = format_value(item.get("value_1"))
        value_2 = format_value(item.get("value_2"))
        children = item.get("children")
        object_type = item.get("type")
        if children:
            result.extend(make_plain(children, key))
        elif object_type == "deleted":
            result.append(f"Property '{key}' was removed")
        elif object_type == "added":
            result.append(f"Property '{key}' was added with value: {value}")
        elif object_type == "update":
            result.append(
                f"Property '{key}' was updated. From {value_1} to {value_2}"
            )
    return result


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
