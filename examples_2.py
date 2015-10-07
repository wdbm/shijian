#!/usr/bin/env python

from __future__ import division
import shijian
import time

def main():

    list1 = [
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

    numberOfEvents = len(list1)
    progress = shijian.Progress()
    progress.engage_quick_calculation_mode()
    for eventIndex, event in enumerate(list1):
        print(progress.add_datum(fraction = (eventIndex + 1) / numberOfEvents))
        time.sleep(0.5)

if __name__ == '__main__':
    main()
