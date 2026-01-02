# tree.py

A simple Python script to recursively print the structure of a certain directory and its subdirectories in a tree-esque format.

<img src="assets/img/example.png" width=500>

## Dependencies

Python 3.9.6 or higher

## Installation

### Using Command Line (Linux/MacOS/UNIX-like)

Assuming you have ~/bin as a PATH environment variable and python 3 installed, run this in your terminal:
```bash
git clone https://github.com/zeashel/treepy.git
cd treepy
./install.sh
```

You can add an argument to ./install.sh if a different installation path is needed.
```bash
git clone https://github.com/zeashel/treepy.git
cd treepy
./install.sh DIFFERENT/INSTALL/PATH
```

### Manual installation

Install from the releases page, then drag and drop the `tree` file into a directory registered in your PATH. Tip: run `echo $PATH` to view said directories.

## Usage

### Print the structure of the current working directory

```bash
$ tree
```

### Print the structure of a certain directory

```bash
$ tree ~/Projects/example/directory
```

### Include dotfiles
By default, tree ignores dotfiles. Use `-a` or `--all` flag to include them.

```bash
$ tree -a
```

```bash
$ tree ~/Projects/example/directory --all
```

### Subdirectory depth
You can specifiy how many subdirectories you want to recursively print by using `-d` or `--depth` followed by an integer. By default, it is limited to 10, but you can specify any integer you want.

```bash
$ tree -d 3 # only print subdirectories that are no more than 3 directories deep
```

```bash
$ tree --depth 0 # dont print subdirectories (similar to ls command)
```

The [examples](#using-tree--d-0) probably explain this better.

### Saving into a file

Tree only outputs to the stdout. Use output redirection to save to a file.

```bash
tree > tree.txt
```

This saves the output to `tree.txt` instead of dispalying it on the terminal.

## Examples

### Basic usage

Using just `tree` on my portfolio project:

```plaintext
my-portfolio/
├── README.md
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── bloodmoon.js
│   ├── img/
│   │   ├── sample6.jpg
│   │   ├── sample5.jpg
│   │   ├── sample4.jpg
│   │   ├── sample1.jpg
│   │   ├── sample3.jpg
│   │   └── sample2.jpg
│   └── fonts/
│       ├── ebgaramond-italic-variablefont_wght.woff
│       ├── meyne_textur.ttf
│       └── ebgaramond-variablefont_wght.woff
└── pages/
    └── index.html
```

### Using `tree -a -d 1`

This includes dotfiles and limits the subdirectory depth to 1

```plaintext
my-portfolio/
├── .DS_Store
├── README.md
├── .gitignore
├── .git/
│   ├── .DS_Store
│   └── FETCH_HEAD
├── assets/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── fonts/
└── pages/
    └── index.html
```

### Using `tree -d 0`
Limits the subdirectory depth to 0
```plaintext
my-portfolio/
├── README.md
├── assets/
└── pages/
```

### Using `tree -d 1`
Limits the subdirectory depth to 1
```plaintext
my-portfolio/
├── README.md
├── assets/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── fonts/
└── pages/
    └── index.html
```
