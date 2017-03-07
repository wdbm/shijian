#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import setuptools

def main():

    setuptools.setup(
        name             = "shijian",
        version          = "2017.03.07.1448",
        description      = "change, time, file, list, statistics and other utilities",
        long_description = long_description(),
        url              = "https://github.com/wdbm/shijian",
        author           = "Will Breaden Madden",
        author_email     = "wbm@protonmail.ch",
        license          = "GPLv3",
        py_modules       = [
                           "shijian"
                           ],
        install_requires = [
                           "python-dateutil",
                           "numpy",
                           "pyprel",
                           "scipy",
                           "shijian"
                           ],
        entry_points     = """
            [console_scripts]
            shijian = shijian:shijian
        """
    )

def long_description(
    filename = "README.md"
    ):

    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, "rst")
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
