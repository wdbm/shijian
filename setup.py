#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

def main():

    setuptools.setup(
        name             = "shijian",
        version          = "2015.10.29.1755",
        description      = "change and time utilities",
        long_description = (read("README.md")),
        url              = "https://github.com/wdbm/shijian",
        author           = "Will Breaden Madden",
        author_email     = "w.bm@cern.ch",
        license         = "GPLv3"
    )

if __name__ == "__main__":
    main()
