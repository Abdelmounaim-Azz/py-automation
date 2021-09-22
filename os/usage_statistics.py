import sys
import re

logfile = sys.argv[1]
users = {}
with open(logfile) as f:
    for line in f:
        pattern = r"\((\w+)\)$"
        res = re.search(pattern, line)
        name = res[1]
        errP = r"ERROR: "
        error = re.search(errP, line)
        if error is None:
            users[name] = users.get(name, {"Info": 0})
            users[name]["Info"] += 1
        else:
            print("Not implemented")
print(sorted(users.items()))
