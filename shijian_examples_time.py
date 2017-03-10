#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_time                                                        #
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

name    = "shijian_examples_time"
version = "2017-03-09T2350Z"

import datetime

import pyprel
import shijian

def main():

    pyprel.print_line()

    print("current time UTC:\n")
    print(
        shijian.style_datetime_object(
            datetime_object = datetime.datetime.utcnow(),
            style = "HH hours MM minutes SS sounds day DD month YYYY"
        )
    )

    pyprel.print_line()

    year_ICHEP_2016  = 2016
    month_ICHEP_2016 = 8
    day_ICHEP_2016   = 3
    datetime_object_ICHEP_2016_time = datetime.datetime(
        year_ICHEP_2016,
        month_ICHEP_2016,
        day_ICHEP_2016
    )
    datetime_object_current_time_UTC = datetime.datetime.utcnow()
    datetime_object_current_time_UTC_to_ICHEP_2016_time =\
        datetime_object_ICHEP_2016_time - datetime_object_current_time_UTC

    print("time to ICHEP 2016 (DD:HH:MM:SS):\n")
    print(
        shijian.style_datetime_object(
            datetime_object = datetime_object_current_time_UTC_to_ICHEP_2016_time,
            style = "{DD}:{HH}:{MM}:{SS}"
        )
    )

    pyprel.print_line()

    current_time_UTC = shijian.style_datetime_object(
        datetime_object = datetime_object_current_time_UTC,
        style           = "DD:HH:MM:SS"
    )

    print("current time UTC:")
    print(pyprel.render_segment_display(text = current_time_UTC))
    print(" D  D     H  H     M  M     S  S")

    pyprel.print_line()

    current_time_to_ICHEP_2016_time = shijian.style_datetime_object(
        datetime_object = datetime_object_current_time_UTC_to_ICHEP_2016_time,
        style = "{DD}:{HH}:{MM}:{SS}"
    )

    print("time to ICHEP 2016:")
    print(pyprel.render_segment_display(text = current_time_to_ICHEP_2016_time))
    print(" D  D     H  H     M  M     S  S")

    pyprel.print_line()

    timestamp = 1487600377.0
    print("convert UNIX timestamp {timestamp} to YYYY-MM-DDTHHMM".format(
        timestamp = timestamp
    ))
    print(shijian.style_UNIX_timestamp(
        timestamp = timestamp,
        style     = "YYYY-MM-DDTHHMMZ"
    ))

    pyprel.print_line()

if __name__ == '__main__':
    main()
