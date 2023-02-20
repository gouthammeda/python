"""
Author : Prudhvi Akella
Module1
"""

import sys


def test():
    print("This is test function from" + sys.argv[0] + "module")


def add(a: int, b: int) -> int:
    return a + b


def average(number_list) -> int:
    return sum(number_list) / len(number_list)
