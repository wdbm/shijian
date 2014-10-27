################################################################################
#                                                                              #
# shijian                                                                      #
#                                                                              #
################################################################################
#                                                                              #
# version: 2014-10-27T1953Z                                                    #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides elegant printing utilities in Python.                  #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
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

import time
import datetime as datetime

def time_UTC(
    style = None
    ):
    return(
        style_datetime_object(
            datetimeObject = datetime.datetime.utcnow(),
            style = style
        )
    )

def style_datetime_object(
    datetimeObject = None,
    style = "YYYY-MM-DDTHHMMSS"
    ):
    # filename safe
    if style == "YYYY-MM-DDTHHMMSSZ":
        return(datetimeObject.strftime('%Y-%m-%dT%H%M%SZ'))
    # microseconds
    elif style == "YYYY-MM-DDTHHMMSSMMMMMMZ":
        return(datetimeObject.strftime('%Y-%m-%dT%H%M%S%fZ'))
    # elegant
    elif style == "YYYY-MM-DD HH:MM:SS UTC":
        return(datetimeObject.strftime('%Y-%m-%d %H:%M:%SZ'))
    # UNIX time in seconds with second fraction
    elif style == "UNIX time S.SSSSSS":
        return((datetimeObject - datetime.datetime.utcfromtimestamp(0)).total_seconds())
    # UNIX time in seconds rounded
    elif style == "UNIX time S":
        return(int((datetimeObject - datetime.datetime.utcfromtimestamp(0)).total_seconds()))
    # filename safe
    else:
        return(datetimeObject.strftime('%Y-%m-%dT%H%M%SZ'))
