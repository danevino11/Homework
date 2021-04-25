from typing import Any, List

import pytest  

from Homework_2.task3 import all_possible_lists

 
@pytest.mark.parametrize(
    ["args, expected"], 
    [
        (
            [[2, 4], [4, 1], [9, 3]],
            [
                [2, 4, 9],
                [2, 4, 3],
                [2, 1, 9],
                [2, 1, 3],
                [4, 4, 9],
                [4, 4, 3],
                [4, 1, 9],
                [4, 1, 3],
            ],
        ),
    ],
)
def test_combinations(args: List, expected: List[Any]):
    assert all_possible_lists.combinations(args) == expected
