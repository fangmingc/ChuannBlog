
import re


def ppp(filename):
    with open(filename, encoding="utf-8") as rf:
        data = rf.read()
        # print(data)
        # print(re.S)
        # result = re.findall("```.+```.+%.+%.+", data, re.S)
        # print(result)
    data = data.replace("%", "\%")
    with open(filename, "w", encoding="UTF-8") as wf:
        wf.write(data)
    return


ppp("Flask.md")
