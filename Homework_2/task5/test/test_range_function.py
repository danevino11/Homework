import string
from typing import Any, List

import pytest
from Homework_2.task5 import range_function


@pytest.mark.parametrize(
    ["args", "expected"],
    [
        ([string.ascii_lowercase, "f"], ["a", "b", "c", "d", "e"]),
        (
            [string.ascii_lowercase, "f", "o"],
            ["f", "g", "h", "i", "j", "k", "l", "m", "n"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(args: List, expected: List[Any]):
    assert range_function.custom_range(args) == expected
