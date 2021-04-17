import pytest

from homework1.task1.sample_project.calculator import calc


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (187, False), (165, False), ],  # one xtra value to check
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = calc.check_power_of_2(value)

    assert actual_result == expected_result
