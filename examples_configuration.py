#!/usr/bin/env python

import shijian

def main():

    print("\nconfiguration reading examples\n")

    filename_configuration = "example_configuration.md"

    print("open configuration file {filename}".format(
        filename = filename_configuration
    ))
    file_configuration = open(filename_configuration, "r").read()

    print("\nconvert configuration from Markdown list to ordered dictionary:\n")
    configuration = shijian.open_configuration(
        filename = filename_configuration
    )
    print(str(configuration) + "\n")

if __name__ == '__main__':
    main()
