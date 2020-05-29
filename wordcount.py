#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Kano: I spent about 30 minutes completing this assignment.

import sys


def word_counter(filename):
    words = open(filename, "r").read()
    words = words.replace("\n", " ")
    words_list = [x for x in words.split(" ")]
    words_dict = {}
    for x in words_list:
        x = x.lower()
        if x in words_dict.keys():
            words_dict[x] += 1
        else:
            words_dict[x] = 1
    words_list = []
    for x in words_dict:
        words_list.append([x, words_dict[x]])
    return words_list


def print_words(filename):
    words_list = word_counter(filename)
    for x in sorted(words_list):
        print (str(x[0]), str(x[1]))


def print_top(filename):
    words_list = word_counter(filename)
    for x in sorted(words_list, key=lambda x: x[1], reverse=True)[:20]:
        print(str(x[0]), str(x[1]))


def main():
    if len(sys.argv) != 3:
        print ('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
