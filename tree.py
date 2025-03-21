#!/usr/bin/env python3

import os
import sys

def main():
    # cwd
    if len(sys.argv) == 1:
        print_tree(os.getcwd())
    # specified directory
    elif len(sys.argv) == 2:
        if directory_sanitizer(sys.argv[1]):
            print_tree(sys.argv[1])
        else:
            print(f"{sys.arg[1]} is not a valid directory")
    else:
        print("usage: tree || tree <DIR>")

def directory_sanitizer(path):
    try:
        # check if the path is a directory
        if os.path.isdir(path):
            return True
        else:
            return False
    except Exception as e:
        print(f"error checking directory: {e}")
        return False

def print_tree(directory, prefix="", include_dotfiles=False):
    # get a list of all files and directories in the given directory
    items = os.listdir(directory)
    # remove all dot files
    items = [item for item in items if not item.startswith('.')]
    # count the number of items to handle the last item differently
    count = len(items)

    for index, item in enumerate(items):
        # create the full path to the item
        path = os.path.join(directory, item)
        # check if the item is a directory
        is_last = index == count - 1
        # print the tree structure
        print(prefix + ("└── " if is_last else "├── ") + item)
        # if its a directory, recursively print its contents
        if os.path.isdir(path):
            print_tree(path, prefix + ("    " if is_last else "│   "))

if __name__ == "__main__":
    main()
