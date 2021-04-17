import pytest

from Homework_1.task1.sample_project.calculator import calc

def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)
    
def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)    
