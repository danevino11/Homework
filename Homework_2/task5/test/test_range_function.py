import string
from typing import Any, List

import pytest
from Homework_2.task5 import range_function


@pytest.mark.parametrize(
    ["args", "expected"],
    [
        ([string.ascii_lowercase, "g"], ["a", "b", "c", "d", "e", "f"]),
        (
            [string.ascii_lowercase, "g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(args: List, expected: List[Any]):
    assert range_function.custom_range(args) == expected
