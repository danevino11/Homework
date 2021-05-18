import pytest

from Homework_3.task4 import armstrong
 
@pytest.mark.parametrize(
    ["number", "expected"],
    [
        (9, True),
        (153, True),
        (2000, False),
        (0, False),
        (-1, False),
    ],
)
def test_is_armstrong(number: int, expected: bool):
    actual = armstrong.is_armstrong(number)

    assert actual == expected
    
