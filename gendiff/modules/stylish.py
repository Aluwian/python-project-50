import itertools


BASE_SPACE = " "
BASE_SPACE_COUNT = 4
LEFT_OFFSET = 2


def get_indent(num=1):
    return BASE_SPACE * BASE_SPACE_COUNT * num


def stringify(value, level=0):
    if type(value) is not dict:
        return str(value)
    lines = map(lambda item:
                get_indent(level + 1) + str(item[0]) + ': '
                + stringify(item[1], level + 1),
                value.items())
    result = itertools.chain("{", lines,
                             [get_indent(level) + '}'])
    return '\n'.join(result)


def format_value(value, level):
    if type(value) is bool:
        return (str(value)).lower()
    if type(value) is dict:
        return stringify(value, level)
    if value is None:
        return "null"
    return str(value)


def truncate(value):
    if value == "":
        return ""
    return " "


def get_format(data):
    def format_line(array, depth=0):
        lines = []
        for item in array:
            key = item.get("name")
            value = format_value(item.get("value"), (depth + 1))
            value_1 = format_value(item.get("value_1"), (depth + 1))
            value_2 = format_value(item.get("value_2"), (depth + 1))
            children = item.get("children")
            object_type = item.get("type")
            if children:
                body = format_line(children, depth + 1)
                lines.append(f'{get_indent(depth + 1)}{key}: {body}')
            elif object_type == 'deleted':
                lines.append(f'{get_indent(depth) + BASE_SPACE * LEFT_OFFSET}- {key}:{truncate(value)}{value}')
            elif object_type == 'added':
                lines.append(f'{get_indent(depth) + BASE_SPACE * LEFT_OFFSET}+ {key}:{truncate(value)}{value}')
            elif object_type == "update":
                lines.append(
                    f'{get_indent(depth) + BASE_SPACE * LEFT_OFFSET}- {key}:{truncate(value_1)}{value_1}\n'
                    f'{get_indent(depth) + BASE_SPACE * LEFT_OFFSET}+ {key}:{truncate(value_2)}{value_2}')
            elif object_type == 'no-change':
                lines.append(f'{get_indent(depth) + BASE_SPACE * BASE_SPACE_COUNT}{key}:{truncate(value)}{value}')
        result = itertools.chain('{', ['\n'.join(lines)], [get_indent(depth) + '}'])
        return '\n'.join(result)

    return format_line(data, 0)
