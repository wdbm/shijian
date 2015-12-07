# -*- coding: utf-8 -*-
from __future__ import division

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

version = "2015-12-07T1819Z"

import os
import time
import uuid
import datetime
import inspect
import functools
import re
import collections
import math

def _main():
    global clocks
    clocks = Clocks()

def time_UNIX(
    style = "UNIX time S"
    ):
    return style_datetime_object(
        datetimeObject = datetime.datetime.utcnow(),
        style = style
    )

def time_UTC(
    style = None
    ):
    return style_datetime_object(
        datetimeObject = datetime.datetime.utcnow(),
        style = style
    )

def style_datetime_object(
    datetimeObject = None,
    style          = "YYYY-MM-DDTHHMMSS"
    ):
    # filename safe
    if style == "YYYY-MM-DDTHHMMSSZ":
        return datetimeObject.strftime('%Y-%m-%dT%H%M%SZ')
    # microseconds
    elif style == "YYYY-MM-DDTHHMMSSMMMMMMZ":
        return datetimeObject.strftime('%Y-%m-%dT%H%M%S%fZ')
    # elegant
    elif style == "YYYY-MM-DD HH:MM:SS UTC":
        return datetimeObject.strftime('%Y-%m-%d %H:%M:%SZ')
    # UNIX time in seconds with second fraction
    elif style == "UNIX time S.SSSSSS":
        return (datetimeObject -\
            datetime.datetime.utcfromtimestamp(0)).total_seconds()
    # UNIX time in seconds rounded
    elif style == "UNIX time S":
        return int((datetimeObject -\
            datetime.datetime.utcfromtimestamp(0)).total_seconds())
    # filename safe
    else:
        return datetimeObject.strftime('%Y-%m-%dT%H%M%SZ')

def unique3DigitNumber():
    return uniqueNumber(style ="integer 3 significant figures")

def uniqueNumber(
    style = None
    ):
    # mode: integer 3 significant figures
    if style == "integer 3 significant figures":
        initialNumber = 100
        if "uniqueNumbers3SignificantFigures" not in globals():
            global uniqueNumbers3SignificantFigures
            uniqueNumbers3SignificantFigures = []
        if not uniqueNumbers3SignificantFigures:
            uniqueNumbers3SignificantFigures.append(initialNumber)
        else:
            uniqueNumbers3SignificantFigures.append(
                uniqueNumbers3SignificantFigures[-1] + 1
            )
        if\
            style == "integer 3 significant figures" and\
            uniqueNumbers3SignificantFigures[-1] > 999:
            raise Exception
        return uniqueNumbers3SignificantFigures[-1]
    # mode: integer
    else:
        initialNumber = 1
        if "uniqueNumbers" not in globals():
            global uniqueNumbers
            uniqueNumbers = []
        if not uniqueNumbers:
            uniqueNumbers.append(initialNumber)
        else:
            uniqueNumbers.append(uniqueNumbers[-1] + 1)
        return uniqueNumbers[-1]

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
    return fileNameProposed

## @brief return a naturally-sorted list
#  @detail This function returns a naturally-sorted list from an input list.
def natural_sort(listObject): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanumeric_key = lambda key: [
        convert(text) for text in re.split("([0-9]+)", key)
    ]
    return sorted(listObject, key = alphanumeric_key)

## @brief return a naturally-sorted list of filenames that are in a sequence or
## a dictionary of lists of filenames that are in a sequence
def find_file_sequences(
    extension               = "png",
    directory               = ".",
    returnFirstSequenceOnly = True,
    ):
    filenamesOfDirectory = os.listdir(directory)
    filenamesFound = [
        filename for filename in filenamesOfDirectory if re.match(
            r".*\d+.*\." + extension,
            filename
        )
    ]
    filenameSequences = collections.defaultdict(list)
    for filename in filenamesFound:
        pattern = re.sub("\d+", "XXX", filename)
        filenameSequences[pattern].append(filename)
    if returnFirstSequenceOnly is True:
        firstKeyIdentified = filenameSequences.iterkeys().next()
        filenameSequence = natural_sort(filenameSequences[firstKeyIdentified])
        return filenameSequence
    else:
        return filenameSequences

def UID():
    return str(uuid.uuid4())

## @brief return a list of files, directories and subdirectories at a
## specified directory
def directory_listing(
    directory = ".",
    ):
    files_list = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            files_list.append(os.path.join(root, filename))
    return files_list

def normalize(
    x,
    summation = None
    ):
    if summation is None:
        summation = sum(x) # normalize to unity
    return [element/summation for element in x]

def rescale(
    x,
    minimum = 0,
    maximum = 1
    ):
    return [
        minimum + (element - min(x)) * ((maximum - minimum)\
        / (max(x) - min(x))) for element in x
    ]

def indices_of_list_element_duplicates(x):
    seen = set()
    for index, element in enumerate(x):
        if isinstance(element, list):
            element = tuple(element)
        if element not in seen:
            seen.add(element)
        else:
            yield index

def unique_list_elements(x):
    unique_elements = []
    for element in x:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

def composite_variable(x):
    k = len(x) + 1
    variable = 0
    for index, element in enumerate(x):
        variable += k**(index - 1) * element
    return variable

class Clock(object):

    def __init__(
        self,
        name               = None,
        start              = True
        ):
        self._name         = name
        self._start        = start # Boolean start clock on instantiation
        self._startTime    = None # internal (value to return)
        self._startTimeTmp = None # internal (value for calculations)
        self._stopTime     = None # internal (value to return)
        self._updateTime   = None # internal
        # If no name is specified, generate a unique one.
        if self._name is None:
            self._name     = UID()
        # If a global clock list is detected, add a clock instance to it.
        if "clocks" in globals():
            clocks.add(self)
        self.reset()
        if self._start:
            self.start()

    def start(self):
        self._startTimeTmp = datetime.datetime.utcnow()
        self._startTime    = datetime.datetime.utcnow()

    def stop(self):
        self.update()
        self._updateTime   = None
        self._startTimeTmp = None
        self._stopTime     = datetime.datetime.utcnow()

    # Update the clock accumulator.
    def update(self):
        if self._updateTime:        
            self.accumulator += (
                datetime.datetime.utcnow() - self._updateTime
            )
        else:
            self.accumulator += (
                datetime.datetime.utcnow() - self._startTimeTmp
            )
        self._updateTime   = datetime.datetime.utcnow()

    def reset(self):
        self.accumulator   = datetime.timedelta(0)
        self._startTimeTmp = None

    # If the clock has a start time, add the difference between now and the
    # start time to the accumulator and return the accumulation. If the clock
    # does not have a start time, return the accumulation.
    def elapsed(self):
        if self._startTimeTmp:
            self.update()
        return self.accumulator

    def name(self):
        return self._name

    def time(self):
        return self.elapsed().total_seconds()

    def startTime(self):
        if self._startTime:
            return style_datetime_object(datetimeObject = self._startTime)
        else:
            return "none"

    def stopTime(self):
        if self._stopTime:
            return style_datetime_object(datetimeObject = self._stopTime)
        else:
            return "none"

    def report(self):
        string = "clock attribute".ljust(39)      + "value"
        string += "\nname".ljust(40)             + self.name()
        string += "\ntime start (s)".ljust(40)    + self.startTime()
        string += "\ntime stop (s)".ljust(40)     + self.stopTime()
        string += "\ntime elapsed (s)".ljust(40) + str(self.time())
        string += "\n"
        return string

    def printout(self):
        print(self.report())

def timer(function):

    @functools.wraps(function)
    def decoration(
        *args,
        **kwargs
        ):
        arguments = inspect.getcallargs(function, *args, **kwargs)
        clock     = Clock(name = function.__name__)
        result    = function(*args, **kwargs)
        clock.stop()
        return result

    return decoration

class Clocks(object):

    def __init__(
        self
        ):
        self._listOfClocks       = []
        self._defaultReportStyle = "statistics"

    def add(
        self,
        clock
        ):
        self._listOfClocks.append(clock)

    def report(
        self,
        style = None
        ):
        if style is None:
            style = self._defaultReportStyle
        if self._listOfClocks != []:
            if style == "statistics":
                # Create a dictionary of clock types with corresponding lists of
                # times for all instances.
                dictionaryOfClockTypes = {}
                # Get the names of all clocks and add them to the dictionary.
                for clock in self._listOfClocks:
                    dictionaryOfClockTypes[clock.name()] = []
                # Record the values of all clocks for their respective names in
                # the dictionary.
                for clock in self._listOfClocks:
                    dictionaryOfClockTypes[clock.name()].append(clock.time())
                # Create a report, calculating the average value for each clock
                # type.
                string = "clock type".ljust(39) + "mean time (s)"
                for name, values in dictionaryOfClockTypes.items():
                    string += "\n" +\
                              str(name).ljust(39) + str(sum(values)/len(values))
                string += "\n"
            elif style == "full":
                # Create a report, listing the values of all clocks.
                string = "clock".ljust(39) + "time (s)"
                for clock in self._listOfClocks:
                    string += "\n" +\
                              str(clock.name()).ljust(39) + str(clock.time())
                string += "\n"
        else:
            string = "no clocks"
        return string

    def printout(
        self,
        style = None
        ):
        if style is None:
            style = self._defaultReportStyle
        print(self.report(style = style))

def select_spread(
    listOfElements   = None,
    numberOfElements = None
    ):
    """
    This function returns the specified number of elements of a list spread
    approximately evenly.
    """
    if len(listOfElements) <= numberOfElements:
        return listOfElements
    if numberOfElements == 0:
        return []
    if numberOfElements == 1:
        return [listOfElements[int(round((len(listOfElements) - 1) / 2))]]
    return \
        [listOfElements[int(round((len(listOfElements) - 1) /\
        (2 * numberOfElements)))]] +\
        select_spread(listOfElements[int(round((len(listOfElements) - 1) /\
        (numberOfElements))):], numberOfElements - 1)

def split_list(
    list_object = None,
    granularity = None
    ):
    """
    This function splits a list into a specified number of lists. It returns a
    list of lists that correspond to these parts. Negative numbers of parts are
    not accepted and numbers of parts greater than the number of elements in the
    list result in the maximum possible number of lists being returned.
    """
    if granularity < 0:
        raise Exception("negative granularity")
    mean_length = len(list_object) / float(granularity)
    split_list_object = []
    last_length = float(0)
    if len(list_object) > granularity:
        while last_length < len(list_object):
            split_list_object.append(
                list_object[int(last_length):int(last_length + mean_length)]
            )
            last_length += mean_length
    else:
        split_list_object = [[element] for element in list_object]
    return split_list_object

def model_linear(
    data             = None,
    quickCalculation = False
    ):
    if quickCalculation is True:
        data = select_spread(data, 10)
    n = len(data)
    x_values         = []
    y_values         = []
    x_squared_values = []
    xy_values        = []
    for datum in data:
        x = datum[0]
        y = datum[1]
        x_values.append(x)
        y_values.append(y)
        x_squared_values.append(x ** 2)
        xy_values.append(x * y)
    b1 = (sum(xy_values) - (sum(x_values) * sum(y_values)) / n) / \
         (sum(x_squared_values) - (sum(x_values) ** 2) / n)
    b0 = (sum(y_values) - b1 * sum(x_values)) / n
    return (b0, b1)

class Progress():

    def __init__(
        self
        ):
        self.data             = []
        self.quickCalculation = False
        self.updateRate       = 1 # s
        self.clock            = Clock(name = "progress update clock")

    def engage_quick_calculation_mode(
        self
        ):
        self.quickCalculation = True

    def disengage_quick_calculation_mode(
        self
        ):
        self.quickCalculation = False

    def add_datum(
        self,
        fraction = None,
        style    = None
        ):
        if len(self.data) == 0:
            self.data.append((fraction, time_UNIX()))
        elif self.quickCalculation is True:
            time_duration_since_last_update = self.clock.time()
            if time_duration_since_last_update >= self.updateRate:
                self.data.append((fraction, time_UNIX()))
                self.clock.reset()
                self.clock.start()
        else:
            self.data.append((fraction, time_UNIX()))
        return self.status(style = style)

    def estimated_time_of_completion(
        self
        ):
        if len(self.data) <= 1:
            return 0
        else:
            try:
                model_values = model_linear(
                    self.data,
                    quickCalculation = self.quickCalculation
                )
                b0 = model_values[0]
                b1 = model_values[1]
                x = 1
                y = b0 + b1 * x
            except:
                y = 0
            datetimeObject = datetime.datetime.fromtimestamp(int(y))
            return datetimeObject

    # estimated time of arrival
    def ETA(
        self
        ):
        if len(self.data) <= 1:
            return style_datetime_object(
                datetimeObject = datetime.datetime.now()
            )
        else:
            return style_datetime_object(
                datetimeObject = self.estimated_time_of_completion()
            )

    # estimated time remaining
    def ETR(
        self
        ):
        if len(self.data) <= 1:
            return 0
        else:
            delta_time = self.estimated_time_of_completion() - datetime.datetime.now()
            if delta_time.total_seconds() >= 0:
                return delta_time.total_seconds()
            else:
                return 0

    def fraction(
        self
        ):
        return self.data[-1][0]

    def percentage(
        self
        ):
        return 100 * self.fraction()

    def status(
        self,
        style = None
        ):
        if style is None:
            message =\
                "{percentage:.2f}% complete; " +\
                "estimated completion time: {ETA} ({ETR:.2f} s)\r"
            return message.format(
                percentage = self.percentage(),
                ETA        = self.ETA(),
                ETR        = self.ETR()
            )
_main()
