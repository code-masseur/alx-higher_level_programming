#!/usr/bin/python3
def uniq_add(my_list=[]):
    sortedUnique = set(my_list)
    uniqueSum = 0
    for j in sortedUnique:
        uniqueSum += j
    return uniqueSum
