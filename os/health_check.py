import shutil
import psutil
import sys


def check_disk_usage(disk, min_abs, min_percent):
    du = shutil.disk_usage(disk)
    free = 100 * du.free / du.total
    gb_free = du.free / 2**30
    if free < min_percent or gb_free < min_abs:
        return False
    return True


def check_cpu_usage():
    """machine is healthy if cpu usage is less than 75 percent"""
    usage = psutil.cpu_percent(1)
    print("DEBUG:usage:{}".format(usage))
    return usage < 75


if not check_disk_usage("/", 5, 13) or not check_cpu_usage():
    print("ERROR")
    sys.exit(1)

print("All good.")
sys.exit(0)
