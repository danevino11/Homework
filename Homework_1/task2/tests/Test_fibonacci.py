from typing import Sequence

import pytest

from Homework_1.task2 import Fibonacci


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [((1, 1, 2, 3, 5), True), ((-1245, -1000, -531, -34), False), 
     ([0, 0, 0, 1],  False),  ((12, 13, 54, 83), False)]  
)
def test_fibonacci(test_input: Sequence, expected: bool):
    actual = Fibonacci.check_fibonacci(test_input)

    assert actual == expected
