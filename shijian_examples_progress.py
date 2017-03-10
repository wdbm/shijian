#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_progress                                                    #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is shijian examples.                                            #
#                                                                              #
# copyright (C) 2015 Will Breaden Madden, wbm@protonmail.ch                    #
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

from __future__ import division

name    = "shijian_examples_progress"
version = "2017-03-09T2350Z"

import time

import shijian

def main():

    list_1 = [
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30
    ]

    number_of_events = len(list_1)
    progress = shijian.Progress()
    progress.engage_quick_calculation_mode()
    for event_index, event in enumerate(list_1):
        print(progress.add_datum(fraction = (event_index + 1) / number_of_events))
        time.sleep(0.5)

if __name__ == '__main__':
    main()
