#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        newList = []
        for i in matrix:
            modifiedList = list(map((lambda x: x ** 2), i))
            newList.append(modifiedList)
        return newList
