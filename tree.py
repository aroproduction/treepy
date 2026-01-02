#!/usr/bin/env python3

"""
This script is open source under the MIT License.

Copyright (c) 2025 Zahra A. S.
Email: 182934048+zeashel@users.noreply.github.com

tree.py

Recursively prints the structure of a certain directory and subdirectories in a tree-esque format.
"""

from argparse import ArgumentParser
import os

NAME="tree"

def main() -> None:
    """
    Main function of tree.py.

    Args: None
    Returns: None
    """
    args = run_argparse()

    if directory_sanitizer(args.directory):
        print_tree(args.directory, include_dotfiles=args.all, max_depth=args.depth)


def run_argparse() -> ArgumentParser:
    """
    Parse the user's command line arguments. Runs at the beginning of the program.

    Args: None
    Returns: 
        ArgumentParser: an object, parser.parse_args() (parsed arguments)
    """

    parser = ArgumentParser(
        description='''Recursively prints the structure of a certain directory
        and its subdirectories in a tree-esque format. This script is under the 
        MIT License. Copyright (c) 2025 Zahra A. S.''',
        epilog='For more information, see documentation at github.com/zeashel/treepy',
        prog=NAME
    )

    parser.add_argument(
        'directory', nargs='?', default=os.getcwd(), 
        metavar="<DIRECTORY>",
        help='''optional. the path of the directory to print.
        (default: current working directory if not specified).'''
    )

    parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='include hidden files in the tree.'
    )

    parser.add_argument(
        '-d', '--depth', default=10,
        type=int,
        metavar="<INT>",
        help='limit of the subdirectory depth to recursively print (default: 10).'
    )

    return parser.parse_args()

def directory_sanitizer(path: str) -> bool:
    """
    Checks if the provided path is a valid directory.

    Args:
        path (str): The path to the directory to be validated.

    Returns:
        bool: True if the path is a valid directory, False otherwise.
    """
    try:
        # check if the path is a directory
        if os.path.isdir(path):
            return True
        else:
            print(f"error: the directory '{path}' does not exist.")
            return False
    except FileNotFoundError:
        print(f"error: the directory '{path}' does not exist.")
        return False
    except PermissionError:
        print(f"error: you do not have the necessary permissions to access '{path}'.")
        return False
    except OSError as e:
        print(f"error checking directory:\n{e}")
        return False

def print_tree(
    directory: str,
    prefix: str="",
    include_dotfiles: bool=False,
    max_depth: int=10,     # default 10
    current_depth: int=0   # current depth
) -> None:
    """
    Prints the directory and subdirectories structure in a tree-esque format.

    Args:
        directory (str): The path to the directory to be printed.
        prefix (str, optional): The string prefix used for indentation in the output. 
                                Defaults to an empty string.
        include_dotfiles (bool, optional): If True, includes hidden files (dotfiles) 
                                           in the output. Defaults to False.
        max_depth (int, optional): The maximum depth of recursion. Defaults to no limit.
        current_depth (int, optional): The current depth of recursion. Defaults to 0.

    Returns:
        None: This function prints the directory structure to the console.
    """
    if current_depth > max_depth:
        return

    if current_depth == 0:
        # root of the tree
        print(os.path.basename(directory) + "/")

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
        is_last = (index == count - 1) # bool

        # print the tree structure
        print(
            prefix +
            ("└── " if is_last else "├── ") +
            item +
            ("/" if os.path.isdir(path) else "")
        )

        # if its a directory, recursively print its contents
        if os.path.isdir(path):
            # prefix = current prefix + new prefix
            print_tree(
                path,
                prefix + ("    " if is_last else "│   "),
                include_dotfiles,
                max_depth,
                current_depth + 1
            )

if __name__ == "__main__":
    main()
