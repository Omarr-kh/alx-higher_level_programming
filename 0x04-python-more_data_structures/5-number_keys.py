#!/usr/bin/python3
def number_keys(a_dictionary):
    total = 0
    keys = list(a_dictionary.keys())
    for i in keys:
        total += 1
    return total
