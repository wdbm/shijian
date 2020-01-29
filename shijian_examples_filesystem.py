#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_filesystem                                                  #
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

import os
import shijian

def main():

    # files

    filename_1 = "test_file.txt"
    print("attempt to create file {filename} without overwrite".format(
        filename = filename_1
    ))
    filename_1_proposed = shijian.propose_filename(filename = filename_1)
    print("creating file {filename}...".format(
        filename = filename_1_proposed
    ))
    os.mknod(filename_1_proposed)

    print("attempt to create file {filename} without overwrite".format(
        filename = filename_1
    ))
    filename_1_proposed = shijian.propose_filename(filename = filename_1)
    print("creating file {filename}...".format(
        filename = filename_1_proposed
    ))
    os.mknod(filename_1_proposed)

    # directories

    directory_name_1 = "test_directory"
    print("attempt to create directory {directory_name} without overwrite".format(
        directory_name = directory_name_1
    ))
    directory_name_1_proposed = shijian.propose_filename(filename = directory_name_1)
    print("creating file {directory_name}...".format(
        directory_name = directory_name_1_proposed
    ))
    os.makedirs(directory_name_1_proposed)

    print("attempt to create file {directory_name} without overwrite".format(
        directory_name = directory_name_1
    ))
    directory_name_1_proposed = shijian.propose_filename(filename = directory_name_1)
    print("creating file {directory_name}...".format(
        directory_name = directory_name_1_proposed
    ))
    os.makedirs(directory_name_1_proposed)

    # filepaths

    print("filepaths at directory \"media\" with extension \"gif\": {filepaths}".format(
        filepaths = shijian.filepaths_at_directory(
            directory          = "media",
            extension_required = "gif"
        )
    ))

if __name__ == '__main__':
    main()
