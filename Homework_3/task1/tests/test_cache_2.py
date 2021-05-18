from unittest.mock import Mock

import pytest

from Homework_3.task1 import cache_2


@pytest.mark.parametrize("times,expected", [(3, 2), (0, 6), (4, 2), (25, 1)])
def test_caching_function(times, expected):
    m_test = Mock()
    thing = cache_2.cache_func(times)(m_test)
    thing()
    thing()
    thing()
    thing()
    thing()
    thing()
    assert m_test.call_count == expected
