#!/usr/bin/env python
## From: https://stackoverflow.com/questions/45382122/how-to-count-lines-of-code-in-jupyter-notebook
from json import load
from sys import argv

def loc(nb):
    cells = load(open(nb))['cells']
    return sum(len(c['source']) for c in cells)

def run(ipynb_files):
    return sum(loc(nb) for nb in ipynb_files)

if __name__ == '__main__':
    print(run(argv[1:]))