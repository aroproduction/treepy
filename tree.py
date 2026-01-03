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
    Entry point of tree.py.

    Args: None
    Returns: None
    """
    args = run_argparse()

    # TEMP
    if args.verbose:
        print("args.all:", args.all)
        print("args.max_depth:", args.depth)
        print("args.directory_format:", args.directory_format)
        print("ansi_parse(args.directory_format):", repr(ansi_parse(args.directory_format)))

    if directory_sanitizer(args.directory):
        print_tree(
            args.directory,
            include_dotfiles=args.all,
            max_depth=args.depth,
            format_dir=ansi_parse(args.directory_format)
        )

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
        metavar="DIRECTORY",
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

    parser.add_argument(
        '--directory-format', default=[1],
        nargs='*', # 0 or more
        type=int,
        metavar="INT",
        choices=range(0, 256), # 0–53
        help='''0 or more arguments allowed. ANSI escape integer from 0 to 53. 0
        for none, 1 for bold (default), 2 for dim, etc. more info:
        https://en.wikipedia.org/wiki/ANSI_escape_code#Select_Graphic_Rendition_parameters
        (default: 1)''' # TODO: improve help message
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='enable verbose output.'
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

def ansi_parse(args: list) -> str:
    """
    Parse the given list of inters into a single ANSI escape sequence or an empty string.

    Args:
        args (list): List of integers that will be joined into one ANSI escape sequence.

    Returns:
        str: An ANSI escape sequence with the joined integers from args. 
             e.g., [1, 3, 95] -> "\\033[1;3;95m"
        str: If the list contains anything other than an integer, return an empty string.
    """
    try:
        args = [int(x) for x in args]
    except (TypeError, ValueError):
        return ""
    return f"\033[{';'.join(map(str, args))}m"

def print_tree(
    directory: str,
    prefix: str="",
    include_dotfiles: bool=False,
    max_depth: int=10,
    current_depth: int=0,
    format_dir: str="\033[1m" # default bold
) -> None:
    """
    Print the directory and subdirectories structure in a tree-esque format.

    Args:
        directory (str): The path to the directory to be printed.
        prefix (str, optional): The string prefix used for indentation in the output. 
                                Defaults to an empty string.
        include_dotfiles (bool, optional): If True, include hidden files (dotfiles) 
                                           in the output. Defaults to False.
        max_depth (int, optional): The maximum depth of recursion. Defaults to no limit.
        current_depth (int, optional): The current depth of recursion. Defaults to 0.
        format_dir (str, optional): ANSI escape sequence to start directory names.

    Returns:
        None: This function prints the directory structure to the stdout.
    """

    if current_depth == 0:
        # root of the tree
        print(format_dir + os.path.basename(directory) + "/\033[0m")

    if current_depth >= max_depth:
        return

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

        # check if the item is last
        is_last = (index == count - 1) # bool

        # print the tree structure
        print(
            prefix +
            ("└─╴" if is_last else "├─╴") +
            (format_dir if os.path.isdir(path) else "") +
            item +
            ("/\033[0m" if os.path.isdir(path) else ""),
            sep=""
        )

        # if its a directory, recursively print its contents
        if os.path.isdir(path):
            # prefix = current prefix + new prefix
            print_tree(
                path,
                prefix + ("   " if is_last else "│  "),
                include_dotfiles,
                max_depth,
                current_depth + 1,
                format_dir
            )

if __name__ == "__main__":
    main()
