#!/bin/zsh

DIR_USR="$HOME/bin/"

cp tree.py tree
chmod +x tree

if [ -d "$DIR_USR" ]; then
    mv tree "$DIR_USR"
fi

# alternative installation paths to be added later