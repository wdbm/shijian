#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():

    setuptools.setup(
        name             = "shijian",
        version          = "2016.05.12.1337",
        description      = "change and time utilities",
        long_description = Markdown_to_reStructuredText("README.md"),
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

def Markdown_to_reStructuredText(filename):
    try:
        import pypandoc
        return pypandoc.convert(filename, "rst")
    except:
        print("pypandoc not found; long description could be corrupted")
        return read(filename)

if __name__ == "__main__":
    main()
