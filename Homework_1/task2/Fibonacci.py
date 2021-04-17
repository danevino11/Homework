"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    for i in range(len(data) - 2):
        if not data[i] + data[i + 1] == data[i + 2]:  # to exclude all the other cases
            return False
    return True
    
