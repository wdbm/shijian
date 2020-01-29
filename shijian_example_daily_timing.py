#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_example_daily_timing                                                 #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a daily timing example.                                      #
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

usage:
    program [options]

options:
    -h, --help         display help message
    --version          display version and exit
    --dayruntime=TEXT  HHMM--HHMM [default: 1900--0700]
"""

import datetime
import docopt
import time

import shijian

def main(options):
    day_run_time = options["--dayruntime"]
    while True:
        if shijian.in_daily_time_range(time_range = day_run_time):
            print("ok let's do this thing")
            # complex deep learning shit
        else:
            print("i'll wait till it's ma time fam")
            # doin' some other things while chillin'
        time.sleep(1)

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
