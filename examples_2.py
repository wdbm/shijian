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
        fraction = (eventIndex + 1) / numberOfEvents
        progress.add_datum(fraction = fraction)
        time.sleep(0.5)
        print("loaded {percentage:.2f}% of events; estimated completion time: {ETA} ({ETR:.2f} s)\r".format(
            percentage = progress.percentage(),
            ETA        = progress.ETA(),
            ETR        = progress.ETR()
        ))

if __name__ == '__main__':
    main()
