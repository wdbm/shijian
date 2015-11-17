#!/usr/bin/env python

import os
import shijian

def main():

    # files

    filename1="test_file.txt"
    print("attempt to create file {filename} without overwrite".format(
        filename = filename1
    ))
    filename1_proposed = shijian.proposeFileName(fileName = filename1)
    print("creating file {filename}...".format(
        filename = filename1_proposed
    ))
    os.mknod(filename1_proposed)

    print("attempt to create file {filename} without overwrite".format(
        filename = filename1
    ))
    filename1_proposed = shijian.proposeFileName(fileName = filename1)
    print("creating file {filename}...".format(
        filename = filename1_proposed
    ))
    os.mknod(filename1_proposed)

    # directories

    directoryName1="test_directory"
    print("attempt to create directory {directoryName} without overwrite".format(
        directoryName = directoryName1
    ))
    directoryName1_proposed = shijian.proposeFileName(fileName = directoryName1)
    print("creating file {directoryName}...".format(
        directoryName = directoryName1_proposed
    ))
    os.makedirs(directoryName1_proposed)

    print("attempt to create file {directoryName} without overwrite".format(
        directoryName = directoryName1
    ))
    directoryName1_proposed = shijian.proposeFileName(fileName = directoryName1)
    print("creating file {directoryName}...".format(
        directoryName = directoryName1_proposed
    ))
    os.makedirs(directoryName1_proposed)

if __name__ == '__main__':
    main()
