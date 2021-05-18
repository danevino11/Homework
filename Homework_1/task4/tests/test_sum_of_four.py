from typing import List

import pytest

from Homework_1.task4 import sum_of_four


@pytest.mark.parametrize(
    ["test_input", "expected"],
    
    [
    ([1, 2, 3], [-2, -1, -3], [-1, 2, 1], [0, 2, -1], 13), 
    ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 81) 
    ]  
)
def test_fibonacci(a: List[int], b: List[int], c: List[int], d: List[int], expected: int)
    actual = sum_of_four.check_sum_of_four(test_input)

    assert actual == expected
