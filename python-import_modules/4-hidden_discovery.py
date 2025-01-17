#!/usr/bin/python3
import os
import sys

def print_names():
    file_path = "/home/hls/holberton/holbertonschool-higher_level_programming/python-import_modules/hidden_4.pyc"

    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    module = __import__('hidden_4')
    names = dir(module)
    names = [name for name in names if not name.startswith('__')]
    names.sort()
    for name in names:
        print(name)

if __name__ == "__main__":
    print_names()
