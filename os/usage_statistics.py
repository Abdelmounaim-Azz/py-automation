import sys
import re

logfile = sys.argv[1]
error = {}
users = {}
with open(logfile) as f:
    for line in f:
        pattern = r"\((\w+)\)$"
        res = re.search(pattern, line)
        name = res[1]
        user_err = {'Info': 0, 'Error': 0}
        if name not in users:
            users[name] = user_err
        errP = r"ERROR: "
        error = re.search(errP, line)
        if error is None:
            users[name]["Info"] += 1
        elif "ERROR" in line:
            users[name]["Error"] += 1
print(sorted(users.items()))
