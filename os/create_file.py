import os
import sys
filename = sys.argv[1]
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("New file!\n")
else:
    print("Err, the file {} already exists!".format(filename))
    sys.exit(1)
