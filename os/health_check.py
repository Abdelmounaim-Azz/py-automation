import shutil
import psutil


def check_disk_usage(disk):
    """receives a disk to check and return true if there is more than 20 percent free on disk usage or false if it s less """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """machine is healthy if cpu usage is less than 75 percent"""
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("All good.")
