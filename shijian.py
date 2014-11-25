################################################################################
#                                                                              #
# shijian                                                                      #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides change and time utilities in Python.                   #
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

version = "2014-11-25T1204Z"

import os
import time
import uuid as uuid
import datetime as datetime

def time_UNIX(
    style = "UNIX time S"
    ):
    return(
        style_datetime_object(
            datetimeObject = datetime.datetime.utcnow(),
            style = style
        )
    )

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

def unique3DigitNumber():
    return(uniqueNumber(style ="integer 3 significant figures"))

def uniqueNumber(
    style = None
    ):
    if style == "integer 3 significant figures":
        initialNumber = 100
    else:
        initialNumber = 1
    if "uniqueNumbers" not in globals():
        global uniqueNumbers
        uniqueNumbers = []
    if not uniqueNumbers:
        uniqueNumbers.append(initialNumber)
    else:
        uniqueNumbers.append(uniqueNumbers[-1] + 1)
    if style == "integer 3 significant figures" and uniqueNumbers[-1] > 999:
        raise Exception
    return(uniqueNumbers[-1])

## @brief propose a filename
#  @detail This function returns a filename string. If a default filename is not
#  specified, the function generates one based on the current time. If a default
#  filename is specified, the function uses it as the default filename. By
#  default, the function then checks to see if using the filename would cause
#  overwriting of an existing file. If overwriting is possible, the function
#  appends an integer to the filename in a loop in order to generate a filename
#  that would not cause overwriting of an existing file. The function can be set
#  to overwrite instead of using the default overwrite protection behaviour.
#  @return filename string
def proposeFileName(
    fileName  = None,
    overwrite = False
    ):
    # If no file name is specified, generate one.
    if not fileName:
        fileName = time_UTC()
    fileNameProposed = fileName
    if not overwrite:
        count = 0
        while os.path.exists(fileNameProposed):
            count = count + 1
            fileNameDirectory = os.path.dirname(fileName)
            fileNameBase = os.path.splitext(os.path.basename(fileName))[0]
            fileNameExtension = os.path.splitext(os.path.basename(fileName))[1]
            if fileNameDirectory:
                fileNameProposed = fileNameDirectory + \
                                   "/" + \
                                   fileNameBase + \
                                   "_" + \
                                   str(count) + \
                                   fileNameExtension
            else:
                fileNameProposed = fileNameBase + \
                                   "_" + \
                                   str(count) + \
                                   fileNameExtension
    return(fileNameProposed)

def UID():
    return(str(uuid.uuid4()))
