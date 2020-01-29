#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_attributes                                                  #
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

import datetime

import shijian

def main():
    class Event(object):
        pass
    event = Event()
    event.b = [10, 20, 30]
    event.c = 15
    print(shijian.get_attribute(object_instance = event, name = "b[2]"))
    print(shijian.get_attribute(object_instance = event, name = "b"))
    print(shijian.get_attribute(object_instance = event, name = "c"))
    print(shijian.get_attribute(object_instance = event, name = "d"))

if __name__ == '__main__':
    main()
