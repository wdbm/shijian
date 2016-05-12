#!/usr/bin/env python

import datetime

import pyprel
import shijian

def main():

    pyprel.print_line()

    print("current time UTC:\n")
    print(
        shijian.style_datetime_object(
            datetime_object = datetime.datetime.utcnow(),
            style = "HH hours MM minutes SS sounds day DD month YYYY"
        )
    )

    pyprel.print_line()

    year_ICHEP_2016  = 2016
    month_ICHEP_2016 = 8
    day_ICHEP_2016   = 3
    datetime_object_ICHEP_2016_time = datetime.datetime(
        year_ICHEP_2016,
        month_ICHEP_2016,
        day_ICHEP_2016
    )
    datetime_object_current_time_UTC = datetime.datetime.utcnow()
    datetime_object_current_time_UTC_to_ICHEP_2016_time =\
        datetime_object_ICHEP_2016_time - datetime_object_current_time_UTC

    print("time to ICHEP 2016 (DD:HH:MM:SS):\n")
    print(
        shijian.style_datetime_object(
            datetime_object = datetime_object_current_time_UTC_to_ICHEP_2016_time,
            style = "{DD}:{HH}:{MM}:{SS}"
        )
    )

    pyprel.print_line()

    current_time_UTC = shijian.style_datetime_object(
        datetime_object = datetime_object_current_time_UTC,
        style           = "DD:HH:MM:SS"
    )

    print("current time UTC:")
    print(pyprel.render_segment_display(text = current_time_UTC))
    print(" D  D     H  H     M  M     S  S")

    pyprel.print_line()

    current_time_to_ICHEP_2016_time = shijian.style_datetime_object(
        datetime_object = datetime_object_current_time_UTC_to_ICHEP_2016_time,
        style = "{DD}:{HH}:{MM}:{SS}"
    )

    print("time to ICHEP 2016:")
    print(pyprel.render_segment_display(text = current_time_to_ICHEP_2016_time))
    print(" D  D     H  H     M  M     S  S")

    pyprel.print_line()

if __name__ == '__main__':
    main()