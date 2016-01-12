#!/usr/bin/env python

from __future__ import division
import shijian
import time

def main():

    list_1 = [
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30,
        30
    ]

    number_of_events = len(list_1)
    progress = shijian.Progress()
    progress.engage_quick_calculation_mode()
    for event_index, event in enumerate(list_1):
        print(progress.add_datum(fraction = (event_index + 1) / number_of_events))
        time.sleep(0.5)

if __name__ == '__main__':
    main()
