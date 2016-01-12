#!/usr/bin/env python

import os
import shijian

def main():

    # files

    filename_1="test_file.txt"
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

    directory_name_1="test_directory"
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

if __name__ == '__main__':
    main()
