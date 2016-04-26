#!/usr/bin/env python

import datetime
import os

import shijian

def main():

    print("\ntime styles:\n")
    datetime_object_current_time_UTC = datetime.datetime.utcnow()
    styles = [
        "YYYY-MM-DDTHHMMSSZ",
        "YYYY-MM-DDTHHMMSSMMMMMMZ",
        "YYYY-MM-DD HH:MM:SS UTC",
        "UNIX time S.SSSSSS",
        "UNIX time S",
        "day DD month YYYY",
        "HH:MM day DD month YYYY",
        "HH:MM:SS day DD month YYYY",
        "day DD month YYYY HH:MM:SS",
        "HH hours MM minutes SS sounds day DD month YYYY",
        "HH:MM:SS",
        "HH hours MM minutes SS seconds",
        "YYYY-MM-DDTHHMMZ",
        "YYYY-MM-DDTHHMMSSZ"
    ]
    for style in styles:
        print(shijian.style_datetime_object(
            datetime_object = datetime_object_current_time_UTC,
            style           = style
        ))

if __name__ == '__main__':
    main()
