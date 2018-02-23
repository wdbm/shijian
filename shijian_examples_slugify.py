#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_slugify                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is shijian examples.                                            #
#                                                                              #
# copyright (C) 2018 Will Breaden Madden, wbm@protonmail.ch                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

import shijian

name    = "shijian_examples_slugify"
version = "2018-02-23T0411Z"

def main():

    for text in [
        "This is some text.",
        "This is an awkward ******* filename."
        ]:
        print("\noriginal text:")
        print(text)
        print("slugified text for filename:")
        print(shijian.slugify(text))

    for text in [
        "This is some text.",
        "This_is_an awkward ******* URL."
        ]:
        print("\noriginal text:")
        print(text)
        print("slugified text for URL:")
        print(shijian.slugify(text))

if __name__ == '__main__':
    main()
