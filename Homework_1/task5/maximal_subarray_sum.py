"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    nums.sort()
    last = nums[len(nums)-(k-2)]
    second_last = nums[len(nums) - (k-1)]
    third_last = nums[len(nums) - k]
    if last >= last + second_last:    # in case the third-to-last element is less than/equal to zero
        return last
    if last + second_last >= last + second_last + third_last:    # in case the third-to-last and second-to-last elements are less than/equal to zero
        return last + second_last
    return  last + second_last + third_last
