import pytest

from Homework_1.task1.sample_project.calculator import calc


@pytest.mark.parametrize(
    ["test_input", "expected"],
    [(65536, True), (12, False), (321, False), (-1245, False)]  # Two xtra numbers to check
)
def test_power_of_2(test_input: int, expected: bool):
    actual = calc.check_power_of_2(test_input)

    assert actual == expected
