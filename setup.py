#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools
import pypandoc

def main():

    setuptools.setup(
        name             = "shijian",
        version          = "2015.10.30.1635",
        description      = "change and time utilities",
        long_description = pypandoc.convert("README.md", "rst"),
        url              = "https://github.com/wdbm/shijian",
        author           = "Will Breaden Madden",
        author_email     = "w.bm@cern.ch",
        license          = "GPLv3",
        py_modules       = ["shijian"],
        entry_points     = """
            [console_scripts]
            shijian = shijian:shijian
        """
    )

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

if __name__ == "__main__":
    main()
