from typing import List, Tuple

import pytest  

from Homework_2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["values", "expected"], 
    [[4, 5, 3, 5, 5, 5, 9, 5, 5, 5, 1, 2], (5, 4)]
)
def test_major_and_minor_elem(values: List[int], expected: Tuple[int, int]):
    assert major_and_minor_elem(values) == expected
