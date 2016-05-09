#!/usr/bin/env python

import shijian

def main():

    number = 1234567890123
    print("number {number} in English text:\n{number_text}".format(
        number = number,
        number_text = shijian.number_to_English_text(number)
    ))

if __name__ == "__main__":
    main()