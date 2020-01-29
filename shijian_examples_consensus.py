#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_consensus                                                   #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is shijian examples.                                            #
#                                                                              #
# copyright (C) 2016 Will Breaden Madden, wbm@protonmail.ch                    #
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

import sys

import pyprel
import shijian

def main():
    sentences = shijian.List_Consensus([
        "This is a test.",
        "This test.",
        "This is a test.",
        "This is not a test.",
        "This is a test.",
        "This is a test.",
        "This is a test.",
        "This is a test.",
        "This is a test.",
        "This is a test."
    ])
    print("list:\n{list}".format(list = sentences))
    print("list size: {size}".format(size = sys.getsizeof(sentences)))
    print("list consensus: {consensus}".format(consensus = sentences.consensus()))
    print("ensure list size...")
    sentences.ensure_size()
    pyprel.print_line()
    print("append to list multiple times while ensuring list size...")
    print("list:\n{list}".format(list = sentences))
    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))
    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))
    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))
    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))
    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))
    pyprel.print_line()
    print("list:\n{list}".format(list = sentences))

if __name__ == '__main__':
    main()
