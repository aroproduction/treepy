#!/usr/bin/env python3

import os
import sys

def main():
    args_amount = len(sys.argv)

    # check for -a or --all flag in the last arg
    if sys.argv[args_amount - 1] in ["-a", "--all"]:
        is_all = True
    else:
        is_all = False

    # print cwd if no directory specified
    if args_amount == 1:
        print_tree(os.getcwd())
    elif args_amount == 2 and is_all is True:
        print_tree(os.getcwd(), include_dotfiles=is_all)

    # specified directory
    elif args_amount == 2 and is_all is False:
        if directory_sanitizer(sys.argv[1]):
            print_tree(sys.argv[1])
        else:
            print(f"{sys.argv[1]} is not a valid directory")
    elif args_amount == 3 and is_all is True:
        if directory_sanitizer(sys.argv[1]):
            print_tree(sys.argv[1], include_dotfiles=is_all)
        else:
            print(f"{sys.argv[1]} is not a valid directory")
    else:
        print("usage: tree || tree <DIR> [-a | --all]")

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
    if include_dotfiles is False:
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
