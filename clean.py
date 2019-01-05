#!/usr/bin/python3

import os, shutil

ROOT = "."

PATTERNS = [".pyc", "__pycache__"]

BOLD = '\033[1m'
ENDC = '\033[0m'

TEMPLATE = "%s -- %s"

def main():
    recurse(ROOT, PATTERNS)

def bold(s):
    return BOLD + s + ENDC

def report(d, t, f):
    t = ["F", "D"][t]
    temp = TEMPLATE % (t, f)
    if d:
        temp = bold(temp)
    print(temp)

def recurse(f, patterns):
    t = os.path.isdir(f)
    if t:
        d = matches(f, patterns)
        report(d, t, f)
        if d:
            shutil.rmtree(f)
        else:
            for fname in os.listdir(f):
                newf = os.path.join(f, fname)
                recurse(newf, patterns)
    else:
        d = matches(f, patterns)
        if d:
            os.remove(f)
        report(d, t, f)
        

def matches(f, patterns):
    for pattern in patterns:
        if f.endswith(pattern):
            return True
    return False

if __name__ == "__main__":
    main()
