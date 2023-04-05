import itertools

BASE_SPACE = " "
BASE_SPACE_COUNT = 4
LEFT_OFFSET = 2


def get_indent(num=1):
    return BASE_SPACE * BASE_SPACE_COUNT * num


def stringify(value, level=0):
    if type(value) is not dict:
        return str(value)
    lines = map(
        lambda item: f"{get_indent(level + 1)}{str(item[0])}: "
        f"{stringify(item[1], level + 1)}",
        value.items(),
    )
    result = itertools.chain("{", lines, [get_indent(level) + "}"])
    return "\n".join(result)


def format_value(value, level):
    if type(value) is bool:
        return (str(value)).lower()
    if type(value) is dict:
        return stringify(value, level)
    if value is None:
        return "null"
    return str(value)


def format_changes(dictionary, level):
    key = dictionary.get("name")
    object_type = dictionary.get("type")
    value = format_value(dictionary.get("value"), (level + 1))
    value_1 = format_value(dictionary.get("value_1"), (level + 1))
    value_2 = format_value(dictionary.get("value_2"), (level + 1))
    if object_type == "deleted":
        return (
            f"{get_indent(level) + BASE_SPACE * LEFT_OFFSET}- "
            f"{key}: {value}"
        )
    elif object_type == "added":
        return (
            f"{get_indent(level) + BASE_SPACE * LEFT_OFFSET}+ "
            f"{key}: {value}"
        )
    elif object_type == "update":
        return (
            f"{get_indent(level) + BASE_SPACE * LEFT_OFFSET}- "
            f"{key}: {value_1}\n"
            f"{get_indent(level) + BASE_SPACE * LEFT_OFFSET}+ "
            f"{key}: {value_2}"
        )
    return (
        f"{get_indent(level) + BASE_SPACE * BASE_SPACE_COUNT}" f"{key}: {value}"
    )


def get_stylish_format(data):
    def format_line(array, depth=0):
        lines = []
        for item in array:
            key = item.get("name")
            children = item.get("children")
            if children:
                body = format_line(children, depth + 1)
                lines.append(f"{get_indent(depth + 1)}{key}: {body}")
            else:
                lines.append(format_changes(item, depth))
        result = itertools.chain(
            "{", ["\n".join(lines)], [get_indent(depth) + "}"]
        )
        return "\n".join(result)

    return format_line(data, 0)
