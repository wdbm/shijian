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
# This program provides change, time, file, list, statistics and other         #
# utilities.                                                                   #
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

name    = "shijian"
version = "2017-03-07T1448Z"

import collections
import datetime
import functools
import inspect
import math
import os
import pickle
import random
import re
import subprocess
import sys
import time
import unicodedata
import uuid

import dateutil.relativedelta
import numpy
import scipy.interpolate
import scipy.io.wavfile

def _main():
    global clocks
    clocks = Clocks()

def time_UNIX(
    style = "UNIX time S"
    ):
    return style_datetime_object(
        datetime_object = datetime.datetime.utcnow(),
        style           = style
    )

def time_UTC(
    style = None
    ):
    return style_datetime_object(
        datetime_object = datetime.datetime.utcnow(),
        style           = style
    )

def filename_time_UNIX(
    style = "UNIX time S.SSSSSS",
    extension = None
    ):
    filename = str(
        time_UNIX(
            style = style
        )
    )
    if extension:
        filename = filename + extension
    filename_proposed = propose_filename(
        filename = filename
    )
    return filename_proposed

def filename_time_UTC(
    style     = "YYYY-MM-DDTHHMMSSZ",
    extension = None
    ):
    filename = style_datetime_object(
        datetime_object = datetime.datetime.utcnow(),
        style           = style
    )
    if extension:
        filename = filename + extension
    filename_proposed = propose_filename(
        filename = filename
    )
    return filename_proposed

def style_minimal_seconds(seconds):
    time_intervals = ["days", "hours", "minutes", "seconds"]
    dateutil_object = dateutil.relativedelta.relativedelta(seconds = seconds)
    return " ".join("{} {}".format(
        getattr(dateutil_object, interval), interval
    ) for interval in time_intervals if getattr(dateutil_object, interval))

def style_UNIX_timestamp(
    timestamp = None,
    style     = "YYYY-MM-DDTHHMMZ"
    ):
    return style_datetime_object(
        datetime_object = datetime.datetime.utcfromtimestamp(timestamp),
        style           = style
    )

def style_datetime_object(
    datetime_object = None,
    style           = "YYYY-MM-DDTHHMMZ"
    ):

    if type(datetime_object) is datetime.datetime:

        # filename safe
        if style == "YYYY-MM-DDTHHMMZ":
            return datetime_object.strftime("%Y-%m-%dT%H%MZ")
        # filename safe with seconds
        elif style == "YYYY-MM-DDTHHMMSSZ":
            return datetime_object.strftime("%Y-%m-%dT%H%M%SZ")
        # filename safe with seconds and microseconds
        elif style == "YYYY-MM-DDTHHMMSSMMMMMMZ":
            return datetime_object.strftime("%Y-%m-%dT%H%M%S%fZ")
        # elegant
        elif style == "YYYY-MM-DD HH:MM:SS UTC":
            return datetime_object.strftime("%Y-%m-%d %H:%M:%S UTC")
        # elegant
        elif style == "YYYY-MM-DD HH:MM:SS Z":
            return datetime_object.strftime("%Y-%m-%d %H:%M:%S Z")
        # UNIX time in seconds with second fraction
        elif style == "UNIX time S.SSSSSS":
            return (datetime_object -\
                datetime.datetime.utcfromtimestamp(0)).total_seconds()
        # UNIX time in seconds rounded
        elif style == "UNIX time S":
            return int((datetime_object -\
                datetime.datetime.utcfromtimestamp(0)).total_seconds())
        # human-readable date
        elif style == "day DD month YYYY":
            return datetime_object.strftime("%A %d %B %Y")
        # human-readable time and date
        elif style == "HH:MM day DD month YYYY":
            return datetime_object.strftime("%H:%M %A %d %B %Y")
        # human-readable time with seconds and date
        elif style == "HH:MM:SS day DD month YYYY":
            return datetime_object.strftime("%H:%M:%S %A %d %B %Y")
        # human-readable date with time with seconds
        elif style == "day DD month YYYY HH:MM:SS":
            return datetime_object.strftime("%A %d %B %Y %H:%M:%S")
        # human-readable-audible time with seconds and date
        elif style == "HH hours MM minutes SS sounds day DD month YYYY":
            return datetime_object.strftime("%H hours %M minutes %S seconds %A %d %B %Y")
        # human-readable days, hours and minutes
        elif style == "DD:HH:MM":
            return datetime_object.strftime("%d:%H:%M")
        # human-readable days, hours, minutes and seconds
        elif style == "DD:HH:MM:SS":
            return datetime_object.strftime("%d:%H:%M:%S")
        # human-readable time with seconds
        elif style == "HH:MM:SS":
            return datetime_object.strftime("%H:%M:%S")
        # human-readable-audible time with seconds
        elif style == "HH hours MM minutes SS seconds":
            return datetime_object.strftime("%H hours %M minutes %S seconds")
        # filename safe
        else:
            return datetime_object.strftime("%Y-%m-%dT%H%MZ")

    if type(datetime_object) is datetime.timedelta:

        if style == "YYYY-MM-DDTHHMMZ":
            style = "{DD} days, {HH}:{MM}:{SS}"

        if hasattr(datetime_object, "seconds"):
            seconds   = datetime_object.seconds + datetime_object.days * 24 * 3600
        else:
            seconds   = int(datetime_object)

        seconds_total = seconds

        minutes       = int(math.floor(seconds / 60))
        minutes_total = minutes
        seconds      -= minutes * 60

        hours         = int(math.floor(minutes / 60))
        hours_total   = hours
        minutes      -= hours * 60

        days          = int(math.floor(hours / 24))
        days_total    = days
        hours        -= days * 24

        years         = int(math.floor(days / 365))
        years_total   = years
        days         -= years * 365

        return style.format(**{
            "Y"   : years_total,
            "D"   : days_total,
            "H"   : hours_total,
            "M"   : minutes_total,
            "S"   : seconds_total,
            "YYYY": str(years).zfill(4),
            "DD"  : str(days).zfill(2),
            "HH"  : str(hours).zfill(2),
            "MM"  : str(minutes).zfill(2),
            "SS"  : str(seconds).zfill(2)
        })

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

class Clock(object):

    def __init__(
        self,
        name                 = None,
        start                = True
        ):
        self._name           = name
        self._start          = start # Boolean start clock on instantiation
        self._start_time     = None  # internal (value to return)
        self._start_time_tmp = None  # internal (value for calculations)
        self._stop_time      = None  # internal (value to return)
        self._update_time    = None  # internal
        # If no name is specified, generate a unique one.
        if self._name is None:
            self._name = UID()
        # If a global clock list is detected, add a clock instance to it.
        if "clocks" in globals():
            clocks.add(self)
        self.reset()
        if self._start:
            self.start()

    def start(self):
        self._start_time_tmp = datetime.datetime.utcnow()
        self._start_time     = datetime.datetime.utcnow()

    def stop(self):
        self.update()
        self._update_time    = None
        self._start_time_tmp = None
        self._stop_time      = datetime.datetime.utcnow()

    # Update the clock accumulator.
    def update(self):
        if self._update_time:        
            self.accumulator += (
                datetime.datetime.utcnow() - self._update_time
            )
        else:
            self.accumulator += (
                datetime.datetime.utcnow() - self._start_time_tmp
            )
        self._update_time = datetime.datetime.utcnow()

    def reset(self):
        self.accumulator     = datetime.timedelta(0)
        self._start_time_tmp = None

    # If the clock has a start time, add the difference between now and the
    # start time to the accumulator and return the accumulation. If the clock
    # does not have a start time, return the accumulation.
    def elapsed(self):
        if self._start_time_tmp:
            self.update()
        return self.accumulator

    def name(self):
        return self._name

    def time(self):
        return self.elapsed().total_seconds()

    def start_time(self):
        if self._start_time:
            return style_datetime_object(datetime_object = self._start_time)
        else:
            return "none"

    def stop_time(self):
        if self._stop_time:
            return style_datetime_object(datetime_object = self._stop_time)
        else:
            return "none"

    def report(self):
        string = "clock attribute".ljust(39)     + "value"
        string += "\nname".ljust(40)             + self.name()
        string += "\ntime start (s)".ljust(40)   + self.start_time()
        string += "\ntime stop (s)".ljust(40)    + self.stop_time()
        string += "\ntime elapsed (s)".ljust(40) + str(self.time())
        string += "\n"
        return string

    def printout(self):
        print(self.report())

class Clocks(object):

    def __init__(
        self
        ):
        self._list_of_clocks       = []
        self._default_report_style = "statistics"

    def add(
        self,
        clock
        ):
        self._list_of_clocks.append(clock)

    def report(
        self,
        style = None
        ):
        if style is None:
            style = self._default_report_style
        if self._list_of_clocks != []:
            if style == "statistics":
                # Create a dictionary of clock types with corresponding lists of
                # times for all instances.
                dictionary_of_clock_types = {}
                # Get the names of all clocks and add them to the dictionary.
                for clock in self._list_of_clocks:
                    dictionary_of_clock_types[clock.name()] = []
                # Record the values of all clocks for their respective names in
                # the dictionary.
                for clock in self._list_of_clocks:
                    dictionary_of_clock_types[clock.name()].append(clock.time())
                # Create a report, calculating the average value for each clock
                # type.
                string = "clock type".ljust(39) + "mean time (s)"
                for name, values in dictionary_of_clock_types.items():
                    string += "\n" +\
                        str(name).ljust(39) + str(sum(values)/len(values))
                string += "\n"
            elif style == "full":
                # Create a report, listing the values of all clocks.
                string = "clock".ljust(39) + "time (s)"
                for clock in self._list_of_clocks:
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
            style = self._default_report_style
        print(self.report(style = style))

class Progress():

    def __init__(
        self
        ):
        self.data              = []
        self.quick_calculation = False
        self.update_rate       = 1 # s
        self.clock             = Clock(name = "progress update clock")

    def engage_quick_calculation_mode(
        self
        ):
        self.quick_calculation = True

    def disengage_quick_calculation_mode(
        self
        ):
        self.quick_calculation = False

    def add_datum(
        self,
        fraction = None,
        style    = None
        ):
        if len(self.data) == 0:
            self.data.append((fraction, time_UNIX()))
        elif self.quick_calculation is True:
            time_duration_since_last_update = self.clock.time()
            if time_duration_since_last_update >= self.update_rate:
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
                    quick_calculation = self.quick_calculation
                )
                b0 = model_values[0]
                b1 = model_values[1]
                x = 1
                y = b0 + b1 * x
            except:
                y = 0
            datetime_object = datetime.datetime.fromtimestamp(int(y))
            return datetime_object

    # estimated time of arrival
    def ETA(
        self
        ):
        if len(self.data) <= 1:
            return style_datetime_object(
                datetime_object = datetime.datetime.now()
            )
        else:
            return style_datetime_object(
                datetime_object = self.estimated_time_of_completion()
            )

    # estimated time remaining
    def ETR(
        self
        ):
        if len(self.data) <= 1:
            return 0
        else:
            delta_time = \
                self.estimated_time_of_completion() - datetime.datetime.now()
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

def UID():
    return str(uuid.uuid4())

def unique_number(
    style = None
    ):
    # mode: integer 3 significant figures
    if style == "integer 3 significant figures":
        initial_number = 100
        if "unique_numbers_3_significant_figures" not in globals():
            global unique_numbers_3_significant_figures
            unique_numbers_3_significant_figures = []
        if not unique_numbers_3_significant_figures:
            unique_numbers_3_significant_figures.append(initial_number)
        else:
            unique_numbers_3_significant_figures.append(
                unique_numbers_3_significant_figures[-1] + 1
            )
        if\
            style == "integer 3 significant figures" and \
            unique_numbers_3_significant_figures[-1] > 999:
            raise Exception
        return unique_numbers_3_significant_figures[-1]
    # mode: integer
    else:
        initial_number = 1
        if "unique_numbers" not in globals():
            global unique_numbers
            unique_numbers = []
        if not unique_numbers:
            unique_numbers.append(initial_number)
        else:
            unique_numbers.append(unique_numbers[-1] + 1)
        return unique_numbers[-1]

def unique_3_digit_number():
    return unique_number(style = "integer 3 significant figures")

## @brief make text filename or URL safe
def slugify(
    text       = None,
    filename   = True,
    URL        = False,
    return_str = True
    ):
    if type(text) is not unicode:
        text = unicode(text, "utf-8")
    if filename and not URL:
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
        text = unicode(re.sub("[^\w\s-]", "", text).strip())
        text = unicode(re.sub("[\s]+", "_", text))
    elif URL:
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
        text = unicode(re.sub("[^\w\s-]", "", text).strip().lower())
        text = unicode(re.sub("[-\s]+", "-", text))
    if return_str:
        text = str(text)
    return text

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
def propose_filename(
    filename                       = None,
    overwrite                      = False,
    slugify_filename               = True,
    exclude_extension_from_slugify = True
    ):
    # If no file name is specified, generate one.
    if not filename:
        filename = time_UTC()
    filename_proposed = filename
    if slugify_filename:
        if exclude_extension_from_slugify:
            filename_base = os.path.splitext(os.path.basename(filename))[0]
            filename_extension = os.path.splitext(os.path.basename(filename))[1]
            filename_base = slugify(text = filename_base)
            filename_proposed = filename_base + filename_extension
        else:
            filename_proposed = slugify(text = filename)
    if not overwrite:
        count = 0
        while os.path.exists(filename_proposed):
            count = count + 1
            filename_directory = os.path.dirname(filename)
            filename_base = os.path.splitext(os.path.basename(filename))[0]
            filename_extension = os.path.splitext(os.path.basename(filename))[1]
            if filename_directory:
                filename_proposed = filename_directory + \
                                    "/"                + \
                                    filename_base      + \
                                    "_"                + \
                                    str(count)         + \
                                    filename_extension
            else:
                filename_proposed = filename_base      + \
                                    "_"                + \
                                    str(count)         + \
                                    filename_extension
    return filename_proposed

def ensure_platform_release(
    keyphrase  = "el7",
    require    = True,
    warn       = False
    ):
    import platform
    release = platform.release()
    if keyphrase not in release:
        message =\
            "inappropriate environment: " +\
            "\"{keyphrase}\" required; \"{release}\" available".format(
                keyphrase = keyphrase,
                release   = release
            )
        #if warn is True:
            #log.warn(message)
        if require is True:
            #log.fatal(message)
            raise(EnvironmentError)

def ensure_program_available(program):
    #log.debug("ensure program {program} available".format(
    #    program = program
    #))
    if which(program) is None:
        #log.error("program {program} not available".format(
        #    program = program
        #))
        raise(EnvironmentError)
    #else:
        #log.debug("program {program} available".format(
        #    program = program
        #))

def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return(program)
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

def running(program):
    results = subprocess.Popen(
        ["ps", "-A"],
        stdout = subprocess.PIPE
    ).communicate()[0].split("\n")
    matches_current = [
        line for line in results if program in line and "defunct" not in line
    ]
    if matches_current:
        return True
    else:
        return False

def ensure_file_existence(filename):
    #log.debug("ensure existence of file {filename}".format(
    #    filename = filename
    #))
    if not os.path.isfile(os.path.expandvars(filename)):
        #log.fatal("file {filename} does not exist".format(
        #    filename = filename
        #))
        raise(IOError)
    #else:
        #log.debug("file {filename} found".format(
        #    filename = filename
        #))

def rm_file(filename):
    os.remove(filename)

## @brief return a naturally-sorted list of filenames that are in a sequence or
## a dictionary of lists of filenames that are in a sequence
def find_file_sequences(
    extension                  = "png",
    directory                  = ".",
    return_first_sequence_only = True,
    ):
    filenames_of_directory = os.listdir(directory)
    filenames_found = [
        filename for filename in filenames_of_directory if re.match(
            r".*\d+.*\." + extension,
            filename
        )
    ]
    filename_sequences = collections.defaultdict(list)
    for filename in filenames_found:
        pattern = re.sub("\d+", "XXX", filename)
        filename_sequences[pattern].append(filename)
    if return_first_sequence_only is True:
        first_key_identified = filename_sequences.iterkeys().next()
        filename_sequence = \
            natural_sort(filename_sequences[first_key_identified])
        return filename_sequence
    else:
        return filename_sequences

## @brief return a list of files at a specified directory
def ls_files(
    directory = "."
    ):
    return([filename for filename in os.listdir(directory) if os.path.isfile(
        os.path.join(directory, filename)
    )])

## @brief return a list of files, directories and subdirectories at a specified
## directory
def directory_listing(
    directory = ".",
    ):
    files_list = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            files_list.append(os.path.join(root, filename))
    return files_list

def engage_command(
    command = None
    ):
    process = subprocess.Popen(
        [command],
        shell      = True,
        executable = "/bin/bash",
        stdout = subprocess.PIPE
    )
    process.wait()
    output, errors = process.communicate()
    return output

def percentage_power():

    filenames_power = engage_command(
        command = "upower -e"
    )
    filenames_power = [
        line for line in filenames_power.split("\n") if line
    ]

    filenames_power_battery = [
        filename for filename in filenames_power if "battery" in filename
    ]
    filename_power_battery =\
        filenames_power_battery[0] if filenames_power_battery else None

    filenames_power_line = [
        filename for filename in filenames_power if "line" in filename
    ]
    filename_power_line =\
        filenames_power_line[0] if filenames_power_line else None

    if filename_power_battery:
        power_data = engage_command(
            command = "upower -i {filename}".format(
                filename = filename_power_battery
            )
        )
        percentage_power = [
            line for line in power_data.split("\n") if "percentage" in line
        ][0].split()[1]
    elif filename_power_line:
        percentage_power = "100%"
    else:
        percentage_power = None

    return percentage_power

def convert_type_list_elements(
    list_object  = None,
    element_type = str
    ):
    """
    Recursively convert all elements and all elements of all sublists of a list
    to a specified type and return the new list.
    """
    if element_type is str:
        return [str(element) if not isinstance(element, list) else convert_type_list_elements(
            list_object  = element,
            element_type = str
        ) for element in list_object]

class List_Consensus(list):

    """
    This class is designed to instantiate a list of elements. It features
    functionality that limits approximately the memory usage of the list. On
    estimating the size of the list as greater than the specified or default
    size limit, the list reduces the number of elements it contains. The list
    provides functionality to return its most frequent element, which can be
    used to determine its "consensus" element.
    """

    def __init__(
        self,
        *args
        ):
        # list initialisation
        if sys.version_info >= (3, 0):
            super().__init__(self, *args)
        else:
            super(List_Consensus, self).__init__(*args)
        self.size_constraint = 150 # bytes

    def set_size_constraint(
        self,
        size = None
        ):
        if size is not None:
            self.size_constraint = size

    def ensure_size(
        self,
        size = None
        ):
        """
        This function removes the least frequent elements until the size
        constraint is met.
        """
        if size is None:
            size = self.size_constraint
        while sys.getsizeof(self) > size:
            element_frequencies = collections.Counter(self)
            infrequent_element = element_frequencies.most_common()[-1:][0][0]
            self.remove(infrequent_element)

    def append(
        self,
        element,
        ensure_size = True,
        size        = None
        ):
        if size is None:
            size = self.size_constraint
        list.append(self, element)
        if ensure_size:
            self.ensure_size(
                size = size
            )

    def consensus(
        self
        ):
        try:
            element_frequencies = collections.Counter(self)
            return element_frequencies.most_common(1)[0][0]
        except:
            return None

## @brief return a naturally-sorted list
#  @detail This function returns a naturally-sorted list from an input list.
def natural_sort(list_object):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanumeric_key = lambda key: [
        convert(text) for text in re.split("([0-9]+)", key)
    ]
    return sorted(list_object, key = alphanumeric_key)

def indices_of_list_element_duplicates(x):
    seen = set()
    for index, element in enumerate(x):
        if isinstance(element, list):
            element = tuple(element)
        if element not in seen:
            seen.add(element)
        else:
            yield index

def indices_of_greatest_values(
    x,
    number = 5
    ):
    if len(x) <= number:
        number = len(x)
    return [y[0] for y in sorted(enumerate(x), key = lambda y: y[1])[-number:]]

def unique_list_elements(x):
    unique_elements = []
    for element in x:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

def select_spread(
    list_of_elements   = None,
    number_of_elements = None
    ):
    """
    This function returns the specified number of elements of a list spread
    approximately evenly.
    """
    if len(list_of_elements) <= number_of_elements:
        return list_of_elements
    if number_of_elements == 0:
        return []
    if number_of_elements == 1:
        return [list_of_elements[int(round((len(list_of_elements) - 1) / 2))]]
    return \
        [list_of_elements[int(round((len(list_of_elements) - 1) /\
        (2 * number_of_elements)))]] +\
        select_spread(list_of_elements[int(round((len(list_of_elements) - 1) /\
        (number_of_elements))):], number_of_elements - 1)

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

def Markdown_list_to_dictionary(
    Markdown_list = None
    ):
    line = re.compile(r"( *)- ([^:\n]+)(?:: ([^\n]*))?\n?")
    depth = 0
    stack = [{}]
    for indent, name, value in line.findall(Markdown_list):
        indent = len(indent)
        if indent > depth:
            assert not stack[-1], "unexpected indent"
        elif indent < depth:
            stack.pop()
        stack[-1][name] = value or {}
        if not value:
            # new branch
            stack.append(stack[-1][name])
        depth = indent
    return stack[0]

def Markdown_list_to_OrderedDict(
    Markdown_list = None
    ):
    line = re.compile(r"( *)- ([^:\n]+)(?:: ([^\n]*))?\n?")
    depth = 0
    stack = [collections.OrderedDict()]
    for indent, name, value in line.findall(Markdown_list):
        indent = len(indent)
        if indent > depth:
            assert not stack[-1], "unexpected indent"
        elif indent < depth:
            stack.pop()
        stack[-1][name] = value or collections.OrderedDict()
        if not value:
            # new branch
            stack.append(stack[-1][name])
        depth = indent
    return stack[0]

def open_configuration(
    filename = None
    ):
    file_configuration = open(filename, "r").read()
    return Markdown_list_to_OrderedDict(file_configuration)

def change_list_resolution(
    values             = None,
    length             = None,
    interpolation_type = "linear",
    dimensions         = 1
    ):
    y1 = values
    x1 = range(0, len(values))
    interpolation = scipy.interpolate.interp1d(
        x1,
        y1,
        kind = interpolation_type
    )
    x2 = list(numpy.linspace(min(x1), max(x1), length))
    y2 = [float(interpolation(x)) for x in x2]
    if dimensions == 1:
        return y2
    elif dimensions == 2:
        return (x2, y2)

def change_waveform_to_rectangle_waveform(
    values             = None,
    fraction_amplitude = 0.01
    ):
    values[values >= 0] = fraction_amplitude * max(values)
    values[values <  0] = fraction_amplitude * min(values)
    values[:] = [x * (1 / fraction_amplitude) for x in values] 
    return values

def change_sound_file_waveform_to_sound_file_rectangle_waveform(
    filename_waveform           = None,
    filename_rectangle_waveform = None,
    overwrite                   = False,
    fraction_amplitude          = 0.01
    ):
    if filename_rectangle_waveform is None:
        filename_rectangle_waveform = filename_waveform
    filename_rectangle_waveform = propose_filename(
        filename  = filename_rectangle_waveform,
        overwrite = overwrite
    )
    rate, values = scipy.io.wavfile.read(filename_waveform)
    values = change_waveform_to_rectangle_waveform(
        values             = values,
        fraction_amplitude = fraction_amplitude
    )
    values[values >= 0] = fraction_amplitude * max(values)
    values[values <  0] = fraction_amplitude * min(values)
    values[:] = [x * (1 / fraction_amplitude) for x in values] 
    scipy.io.wavfile.write(filename_rectangle_waveform, rate, values)

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

def composite_variable(x):
    k = len(x) + 1
    variable = 0
    for index, element in enumerate(x):
        variable += k**(index - 1) * element
    return variable

def model_linear(
    data              = None,
    quick_calculation = False
    ):
    if quick_calculation is True:
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

def import_object(
    filename  = None
    ):
    return pickle.load(open(filename, "rb"))

def export_object(
    x,
    filename  = None,
    overwrite = False
    ):
    filename = propose_filename(
        filename  = filename,
        overwrite = overwrite
    )
    pickle.dump(x, open(filename, "wb"))

def string_to_bool(x):
    return x.lower() in ("yes", "true", "t", "1")

def number_to_English_text(
    number = None
    ):

    ones =      [
                 "",
                 "one ",
                 "two ",
                 "three ",
                 "four ",
                 "five ",
                 "six ",
                 "seven ",
                 "eight ",
                 "nine "
                ]
    teens =     [
                 "ten ",
                 "eleven ",
                 "twelve ",
                 "thirteen ",
                 "fourteen ",
                 "fifteen ",
                 "sixteen ",
                 "seventeen ",
                 "eighteen ",
                 "nineteen "
                ]
    tens =      [
                 "",
                 "",
                 "twenty ",
                 "thirty ",
                 "forty ",
                 "fifty ",
                 "sixty ",
                 "seventy ",
                 "eighty ",
                 "ninety "
                ]
    thousands = [
                 "",
                 "thousand ",
                 "million ",
                 "billion ",
                 "trillion ",
                 "quadrillion ",
                 "quintillion ",
                 "sextillion ",
                 "septillion ",
                 "octillion ",
                 "nonillion ",
                 "decillion ",
                 "undecillion ",
                 "duodecillion ",
                 "tredecillion ",
                 "quattuordecillion ",
                 "quindecillion",
                 "sexdecillion ",
                 "septendecillion ", 
                 "octodecillion ",
                 "novemdecillion ",
                 "vigintillion "
                ]

    # Split the number into 3-digit groups with each group representing
    # hundreds, thousands etc.
    number_in_groups_of_3 = []
    number_as_string = str(number)
    for position in range(3, 33, 3):
        progressive_number_string = number_as_string[-position:]
        progression = len(number_as_string) - position
        # Break if the end of the number string is encountered.
        if progression < -2:
            break
        else:
            if progression >= 0:
                number_in_groups_of_3.append(int(progressive_number_string[:3]))
            elif progression >= -1:
                number_in_groups_of_3.append(int(progressive_number_string[:2]))
            elif progression >= -2:
                number_in_groups_of_3.append(int(progressive_number_string[:1]))
    # Split the number 3-digit groups into groups of ones, tens etc. and build
    # an English text representation of the number.
    number_words = ""
    for index, group in enumerate(number_in_groups_of_3):
        number_1 = group % 10
        number_2 = (group % 100) // 10
        number_3 = (group % 1000) // 100
        if group == 0:
            continue
        else:
            thousand = thousands[index]
        if number_2 == 0:
            number_words = ones[number_1] + thousand + number_words
        elif number_2 == 1:
            number_words = teens[number_1] + thousand + number_words
        elif number_2 > 1:
            number_words = tens[number_2] + ones[number_1] + thousand + number_words
        if number_3 > 0:
            number_words = ones[number_3] + "hundred " + number_words
    return number_words.strip(" ")

def replace_numbers_in_text_with_English_text(
    text = None
    ):
    # Split the text into text and numbers.
    text = re.split("(\d+)", text)
    if text[-1] == "":
        text = text[:-1]
    text_translated = []
    # Replace numbers with English text.
    for text_segment in text:
        if all(character.isdigit() for character in text_segment):
            text_translated.append(number_to_English_text(number = text_segment))
        else:
            text_translated.append(text_segment)
    return "".join(text_translated)

def pseudorandom_MAC_address():
    return "{aa:02x}:{bb:02x}:{cc:02x}:{dd:02x}:{ee:02x}:{ff:02x}".format(
        aa = random.randint(0, 255),
        bb = random.randint(0, 255),
        cc = random.randint(0, 255),
        dd = random.randint(0, 255),
        ee = random.randint(0, 255),
        ff = random.randint(0, 255)
    )

_main()
