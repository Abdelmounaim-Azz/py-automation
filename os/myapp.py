import os
import subprocess


my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(
    ["/c/Users/admin/Desktop/py-automation/os", my_env["PATH"]])
res = subprocess.run(["myapp"], env=my_env)
print(res.returncode)
