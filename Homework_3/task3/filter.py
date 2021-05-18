# I decided to write a code that generates data filtering object from a list of keyword parameters:
from typing import Dict, List

import pytest

from Homework_3.task3 import filter


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data 
            if all(i(item) for i in self.functions)
        ]

# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        def keyword_filter_func(data, k=key, v=value):
            if k in data:
                return data[k] == v
        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.



def test_filter_output_first():
    """
    Test input: name="Bill", last_name="Gilbert"
    Expecting the first dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual = make_filter(name="Bill", last_name="Gilbert").apply(data)
    expected = [data[0]]
    assert actual == expected


def test_filter_one_key():
    """
    Testing with one key.
    Test input: last_name="Gilbert"
    Expecting the first dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual = make_filter(last_name="Gilbert").apply(data)
    expected = [data[0]]
    assert actual == expected


def test_filter_output_second():
    """
    Test input: name="polly", type="bird"
    Expecting the second dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual = make_filter(name="polly", type="bird").apply(data)
    expected = [data[1]]
    assert actual == expected


def test_filter_one_key_second():
    """
    Testing with one key
    Test input: kind="parrot"
    Expecting the second dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    actual = make_filter(kind="parrot").apply(data)
    expected = [data[1]]
    assert actual == expected


def test_filter_output_third():
    """
    Testing with almost identical dictionaries.
    Test input: name="billy", type="bird"
    Expecting the third dictionary as an output.
    """
    data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
        {"is_dead": False, "kind": "parrot", "type": "bird", "name": "billy"},
    ]

    actual = make_filter(name="billy", type="bird").apply(data)
    expected = [data[2]]
    assert actual == expected