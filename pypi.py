#!/usr/bin/python3

import os, shutil

if __name__ == "__main__":

    DIST = "dist"

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)

    os.system("python3 setup.py sdist")
    os.system("twine upload %s/*" % DIST)
