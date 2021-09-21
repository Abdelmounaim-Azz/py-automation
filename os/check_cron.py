import sys
import re

logfile=sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern=r"USER \((\w+)\)$"
    res=re.search(pattern,logfile)
    print(res[1])