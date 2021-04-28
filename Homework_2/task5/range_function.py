"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(sequence, start=None, finish=None, step=1):
    first = None
    last = None
    num = 0
    values = []
    for i in sequence:
        if i == start:
            first = num
        if i == finish:
            last = num
            break
        values.append(i)
        num += 1
    values = values[first:last:step]
    return values
