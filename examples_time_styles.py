#!/usr/bin/env python

import datetime
import os

import pyprel
import shijian

def main():

    pyprel.print_line()

    print("time styles:")
    datetime_object_current_time_UTC = datetime.datetime.utcnow()
    styles = [
        "YYYY-MM-DDTHHMMSSZ",
        "YYYY-MM-DDTHHMMZ",
        "YYYY-MM-DDTHHMMSSMMMMMMZ",
        "YYYY-MM-DD HH:MM:SS UTC",
        "UNIX time S.SSSSSS",
        "UNIX time S",
        "day DD month YYYY",
        "HH:MM day DD month YYYY",
        "HH:MM:SS day DD month YYYY",
        "day DD month YYYY HH:MM:SS",
        "HH hours MM minutes SS sounds day DD month YYYY",
        "DD:HH:MM",
        "DD:HH:MM:SS",
        "HH:MM:SS",
        "HH hours MM minutes SS seconds"
    ]
    for style in styles:
        print("\nstyle: {style}".format(
            style = style
        ))
        print(shijian.style_datetime_object(
            datetime_object = datetime_object_current_time_UTC,
            style           = style
        ))

    pyprel.print_line()

    print("current time UTC:\n")
    print(shijian.time_UTC(style = "HH hours MM minutes SS sounds day DD month YYYY"))

    pyprel.print_line()

if __name__ == '__main__':
    main()
