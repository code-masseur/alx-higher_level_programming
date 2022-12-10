#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) != 0:
        sortedList = sorted(a_dictionary.keys())
        for x in sortedList:
            print("{}: {}".format(x, a_dictionary[x]))
