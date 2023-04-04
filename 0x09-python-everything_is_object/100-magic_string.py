#!/usr/bin/python3
def array():
    array.n = getattr(array, 'n', 0) + 1
    return ("BestSchool, " * (array.n - 1) + "BestSchool")
