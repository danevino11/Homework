import pytest

from Homework_1.task1.sample_project.calculator import calc


@pytest.mark.parametrize(
    ["number", "expected"],
    [(65536, True), (12, False), (321, False), (-1245, False),]  # Two xtra checks
)
def test_power_of_2(number: int, expected: bool):
    actual_result = calc.check_power_of_2(number)

    assert actual == expected
