"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    list_of_v = []    #     
    with open(file_name) as fi:
        for line in fi:
            list_of_v.append(int((line.strip("\n"))))    # creates a line-by-line list of values
            list_of_v.sort()    # sorts the list
    return list_of_v[0], list_of_v[-1]    # takes first and last elements of a sorted list to create a tuple
        
