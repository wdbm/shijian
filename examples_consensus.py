#!/usr/bin/env python

import sys

import pyprel
import shijian

def main():

    sentences = shijian.List_Consensus([
        "This is a test.",
        "This test.",
        "This is a test.",
        "This is not a test.",
        "This is a test.",
        "This is a test.",
        "This is a test.",
        "This is a test.",
        "This is a test.",
        "This is a test."
    ])

    print("list:\n{list}".format(list = sentences))
    print("list size: {size}".format(size = sys.getsizeof(sentences)))
    print("list consensus: {consensus}".format(consensus = sentences.consensus()))
    print("ensure list size...")
    sentences.ensure_size()

    pyprel.print_line()

    print("append to list multiple times while ensuring list size...")

    print("list:\n{list}".format(list = sentences))

    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))

    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))

    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))

    print("append to list while ensuring list size...")
    sentences.append("This is another test.")
    print("list:\n{list}".format(list = sentences))

    print("append to list while ensuring list size...")
    sentences.append("This is another test.")

    print("list:\n{list}".format(list = sentences))

    pyprel.print_line()

    print("list:\n{list}".format(list = sentences))

if __name__ == '__main__':
    main()
