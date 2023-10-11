#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    keys = list(newDict.keys())

    for q in keys:
        newDict[q] *= 2

    return (newDict)
