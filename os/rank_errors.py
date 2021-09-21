import sys
import re

logfile = sys.argv[1]
errors = {}
with open(logfile) as f:
    for line in f:
        if "ERROR" not in line:
            continue
        pattern1 = r"ERROR: "
        errorIndex = re.search(pattern1, line)
        pattern2 = r"\((\w+)\)$"
        nameIndex = re.search(pattern2, line)
        msgStart = errorIndex.span()[1]
        msgEnd = nameIndex.span()[0]
        errMsg = line[msgStart:msgEnd]
        errors[errMsg.strip()] = errors.get(errMsg.strip(), 0)+1
print(errors)
