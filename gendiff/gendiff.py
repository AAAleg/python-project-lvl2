import json


def bool_format(value):
    if type(value) is bool:
        return str(value).lower()
    return value


def generate_diff(first_file, second_file) -> str:
    result = '{\n'
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    sign = ' '
    for key, value in sorted(file1.items()):
        if key in file1 and key not in file2:
            sign = '-'
            result += f'  {sign} {key}: {bool_format(value)}\n'
        if key in file1 and key in file2 and value != file2[key]:
            sign = '-'
            result += f'  {sign} {key}: {bool_format(value)}\n'
            sign = '+'
            result += f'  {sign} {key}: {bool_format(file2[key])}\n'
        if key in file1 and key in file2 and value == file2[key]:
            sign = ' '
            result += f'  {sign} {key}: {bool_format(file2[key])}\n'
        sign = ' '

    difference = set(file2.keys()).difference(set(file1.keys()))
    for key in sorted(difference):
        sign = '+'
        result += f'  {sign} {key}: {bool_format(file2[key])}\n'
    result += '}'
    return result
