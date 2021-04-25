from typing import Callable
from unittest import mock

from Homework_2.task4 import cache_function


def test_function_cache():
    m = mock.Mock()
    cache_func = cache(m)
    cache_func(100)
    assert m.call_count == 1
