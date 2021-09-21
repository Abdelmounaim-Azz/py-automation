import sys
import re

logfile = sys.argv[1]
users = {}
with open(logfile) as f:
    for line in f:
        pattern = r"\((\w+)\)$"
        res = re.search(pattern, line)
        name = res[1]
        users[name] = users.get(name, 0)+1
print(sorted(users.items()))
