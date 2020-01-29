#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_time_styles                                                 #
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

import datetime
import os

import pyprel
import shijian

def main():
    pyprel.print_line()
    print("time styles:")
    datetime_object_current_time_UTC = datetime.datetime.utcnow()
    styles = [
        "YYYY-MM-DDTHHMMSSZ",
        "YYYY-MM-DDTHHMMZ",
        "YYYY-MM-DDTHHMMSSMMMMMMZ",
        "YYYY-MM-DD HH:MM:SS UTC",
        "UNIX time S.SSSSSS",
        "UNIX time S",
        "day DD month YYYY",
        "HH:MM day DD month YYYY",
        "HH:MM:SS day DD month YYYY",
        "day DD month YYYY HH:MM:SS",
        "HH hours MM minutes SS seconds day DD month YYYY",
        "DD:HH:MM",
        "DD:HH:MM:SS",
        "HH:MM:SS",
        "HH hours MM minutes SS seconds"
    ]
    for style in styles:
        print("\nstyle: {style}".format(
            style = style
        ))
        print(shijian.style_datetime_object(
            datetime_object = datetime_object_current_time_UTC,
            style           = style
        ))
    pyprel.print_line()
    print("current time UTC:\n")
    print(shijian.time_UTC(style = "HH hours MM minutes SS sounds day DD month YYYY"))
    pyprel.print_line()
    print("minimal time style for seconds:\n")
    for seconds in [10, 100, 1000, 10000, 100000]:
        print("{seconds} seconds: {seconds_styled}".format(
            seconds        = seconds,
            seconds_styled = shijian.style_minimal_seconds(seconds)
        ))
    pyprel.print_line()

if __name__ == '__main__':
    main()
