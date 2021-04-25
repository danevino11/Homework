import os

from typing import List

import pytest  

from Homework_2.task1 import (
    get_longest_diverse_words,
    get_rarest_char,
    count_punctuation_chars,
    count_non_ascii_chars,
    get_most_common_non_ascii_char,
    
)
 

@pytest.mark.parametrize(
    "file_name", "expected",
    [
        [
            os.path.join(os.path.dirname(__file__), "test_1.txt"), 
            [
                'yghrfbhavjnbajtbnisbn', 
                'wgiunibuth54uhgt', 
                'kmvjdjkvcckhsfdih', 
                'brbisuhbiufgnbfgbfnfgn', 
                'bbgfieooutr', 
                'ghbnghtbsrngdssbrtbfgb', 
                'bstiubsbiujrs', 
                'aiousbj', 
                'bgbsfnbjgsngbgfbsdbsgbsgbsgb', 
                'gbsbbsibnsliu'
            ],         
        ],
    ]
)
def test_get_longest_diverse_words(file_name: str, expected: List[str]):
    assert get_longest_diverse_words(file_name) == expected
    
    
@pytest.mark.parametrize(
    "file_name", "expected",
    [
        [os.path.join(os.path.dirname(__file__), "test_2.txt"), "Y"],
        
        
    ],
)
def test_get_rarest_char(file_name: str, expected: str):
    assert get_rarest_char(file_name) == expected   
    
    
@pytest.mark.parametrize(
    "file_name", "expected",
    [
        [os.path.join(os.path.dirname(__file__), "test_3.txt"), 53],
        
        
    ],
)
def test_count_punctuation_chars(file_name: str, expected: int):
    assert count_punctuation_chars(file_name) == expected   
    
    
@pytest.mark.parametrize(
    "file_name", "expected",
    [
        [os.path.join(os.path.dirname(__file__), "test_4.txt"), 6],
        
        
    ],
)
def test_count_non_ascii_chars(file_name: str, expected: int):
    assert count_non_ascii_chars(file_name) == expected       
    
    
@pytest.mark.parametrize(
    "file_name", "expected",
    [
        [os.path.join(os.path.dirname(__file__), "test_5.txt"), "П"],
        
        
    ],
)
def test_get_most_common_non_ascii_char(file_name: str, expected: str):
    assert get_most_common_non_ascii_char(file_name) == expected
    
