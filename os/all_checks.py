#!/usr/bin/env python3

import os
import shutil
import sys


def check_reboot():
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    # percentage of free space
    percent_free = 100 * du.free / du.total
    # free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return False
    return True


def check_root_full():
    return check_disk_full(disk="/", min_gb=2, min_percent=10)


def main():
    checks = [(check_reboot, "Pending Reboot"),
              (check_root_full, "Root partition full")]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("All good")
    sys.exit(0)


main()