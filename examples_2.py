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
        30
    ]

    progress = shijian.Progress()
    numberOfElements = len(list1)
    for index, element in enumerate(list1):
        time.sleep(1)
        fraction = (index + 1) / numberOfElements
        progress.add_datum(fraction = fraction)
        print("progress: {percentage:.2f}%, ETA: {ETA}, ETR: {ETR:.2f} s".format(
            percentage = progress.percentage(),
            ETA        = progress.ETA(),
            ETR        = progress.ETR()
        ))

if __name__ == '__main__':
    main()
