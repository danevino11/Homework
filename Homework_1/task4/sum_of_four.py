"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        number_of_tuples = 0
        dict_of_tuples = {}
        for i in a:
            for j in b:
                sums = i + j
                dict_of_tuples[sums] = dict_of_tuples.get(sums, 0) + 1
                print(dict_of_tuples)
        
        for k in c:
            for l in d:
                sums = k + l
                if -sums in dict_of_tuples:
                    number_of_tuples += dict_of_tuples[-sums]      
        return number_of_tuples
