import re


def rearrange_name(name):
    res = re.search(r"^([\w .-*]),([\w .-*])$", name)
    if res == None:
        return name
    return "{} {}".format(res[2], res[1])


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    res = re.search(regex, log_line)
    if res == None:
        return ""
    return res[1]
