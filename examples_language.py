#!/usr/bin/env python

import pyprel
import shijian

def main():

    pyprel.print_line()

    number = 1234567890123
    print("number {number} in English text:\n{number_text}".format(
        number = number,
        number_text = shijian.number_to_English_text(number)
    ))

    pyprel.print_line()

    text = "It is 03:14 and I have 3 apples in 400 wormholes."
    print("replace numbers with English text in the following text:\n{text}".format(
        text = text
    ))
    print(shijian.replace_numbers_in_text_with_English_text(text = text))

    pyprel.print_line()

if __name__ == "__main__":
    main()