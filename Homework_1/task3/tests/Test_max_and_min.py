import os

from typing import Sequence

import pytest

from Homework_1.task3 import find_min_and_max

print(os.path.dirname(__file__))


@pytest.mark.parametrize(
    "file_name, expected",
    [
        [os.path.join(os.path.dirname(__file__), "test_1.txt"), (1, 743)],
        [os.path.join(os.path.dirname(__file__), "test_2.txt"), (-9, 11)],
        [os.path.join(os.path.dirname(__file__), "test_3.txt"), (-58, 1154)]
        
    ],
)
def test_maximum_and_minimum(file_name, expected):
    assert find_min_and_max.find_maximum_and_minimum(file_name) == expected
