import json
import re
from gendiff.modules.parser import get_file


def generate_diff(path_1, path_2):
    (data_1, form) = get_file(path_1)
    (data_2, form) = get_file(path_2)
    keys = sorted(data_1.keys() | data_2.keys())
    answer = {}
    for key in keys:
        if key not in data_1:
            answer["+ " + key] = data_2[key]
        elif key not in data_2:
            answer["- " + key] = data_1[key]
        elif data_1[key] == data_2[key]:
            answer["  " + key] = data_1[key]
        else:
            answer["- " + key] = data_1[key]
            answer["+ " + key] = data_2[key]
    return re.sub('"|,', "", json.dumps(answer, indent=2))
