import argparse
import re


def task3():
    result = ""
    _bool = True
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, type=str, help="Name of file")
    p = parser.parse_args()
    c = re.compile(r'%quit')
    while _bool:
        _str = str(input())
        if c.findall(_str):
            _str = _str[:_str.find("%quit")]
            result += _str
            _bool = False
        else:
            result += _str + "\n"
    file = open(p.file, 'w')
    file.write(result)
    file.close()
    return result


print(task3())