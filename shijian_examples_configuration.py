#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_configuration                                               #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is shijian examples.                                            #
#                                                                              #
# copyright (C) 2017 Will Breaden Madden, wbm@protonmail.ch                    #
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

name    = "shijian_examples_configuration"
version = "2017-03-09T2350Z"

import shijian

def main():

    print("\nconfiguration reading examples\n")

    filename_configuration = "example_configuration.md"

    print("open configuration file {filename}".format(
        filename = filename_configuration
    ))
    file_configuration = open(filename_configuration, "r").read()

    print("\nconvert configuration from Markdown list to ordered dictionary:\n")
    configuration = shijian.open_configuration(
        filename = filename_configuration
    )
    print(str(configuration) + "\n")

if __name__ == '__main__':
    main()
