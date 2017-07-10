#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# shijian_examples_language                                                    #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is shijian examples.                                            #
#                                                                              #
# copyright (C) 2016 Will Breaden Madden, wbm@protonmail.ch                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

import pyprel
import shijian

name    = "shijian_examples_language"
version = "2017-07-10T2155Z"

def main():

    pyprel.print_line()

    number = 1234567890123
    print("number {number} in English text:\n\n{number_text}".format(
        number = number,
        number_text = shijian.number_to_English_text(number)
    ))

    pyprel.print_line()

    text = "It is 03:14 and I have 3 apples in 400 wormholes."
    print("replace numbers with English text in the following text:\n{text}\n".format(
        text = text
    ))
    print(shijian.replace_numbers_in_text_with_English_text(text = text))

    pyprel.print_line()

    text = "I've ten important invasions to consider."
    print("change contractions to full words and change numbers to digits in the following text:\n{text}\n".format(
        text = text
    ))
    print(shijian.replace_contractions_with_full_words_and_replace_numbers_with_digits(text = text))

    pyprel.print_line()

if __name__ == "__main__":
    main()
