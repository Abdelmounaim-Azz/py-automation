import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        res = re.search(pattern, logfile)
        if res is None:
            continue
        name = res[1]
        usernames[name] = usernames.get(name, 0)+1
print(usernames)
