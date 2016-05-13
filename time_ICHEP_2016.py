#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
# time_ICHEP_2016                                                              #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program gives the time to ICHEP 2016.                                   #
#                                                                              #
# copyright (C) 2016 William Breaden Madden                                    #
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

name    = "time_ICHEP_2016"
version = "2016-05-13T0310Z"

import datetime
import os
import time

import pyprel
import shijian

def main():

    while True:

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

        current_time_to_ICHEP_2016_time = shijian.style_datetime_object(
            datetime_object = datetime_object_current_time_UTC_to_ICHEP_2016_time,
            style = "{DD}:{HH}:{MM}:{SS}"
        )

        print("time to ICHEP 2016:")
        print(pyprel.render_segment_display(text = current_time_to_ICHEP_2016_time))
        print(" D  D     H  H     M  M     S  S")

        time.sleep(1)
        os.system("tput reset")

if __name__ == '__main__':
    main()