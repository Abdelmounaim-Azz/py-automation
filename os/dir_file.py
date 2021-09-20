import os


def file_dir(dir):
    for name in os.listdir(dir):
        fullpath = os.path.join(dir, name)
        if os.path.isdir(fullpath):
            print("{} is a directory".format(fullpath))
        else:
            print("{} is a file".format(fullpath))


file_dir("py-automation")
