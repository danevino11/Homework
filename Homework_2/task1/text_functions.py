"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char 
    5) Find most common non ascii char for document
"""
import tokenize
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = []
    with open(file_path) as fi:
        tokens = tokenize.generate_tokens(fi.readline)
        for token in tokens:
            if token.type == 1:
                words.append([token.string, len(set(token.string))])
    words.sort(key=lambda x: x[1], reverse=True)
    result = []
    for i in range(10):
        result.append(words[i][0])
    return result


def get_rarest_char(file_path: str) -> str:
    char = {}
    with open(file_path) as fi:
        for line in fi:
            for i in line:
                if i not in char:
                    char[i] = 1
                else:
                    char[i] += 1
    return min(char, key=char.get)


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as fi:
        for line in fi:
            for i in line:
                if i in punctuation:
                    count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as fi:
        for line in fi:
            for i in line:
                if not i.isascii():
                    count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    char = {}
    with open(file_path) as fi:
        for line in fi:
            for i in line:
                if not i.isascii():
                    if i not in char:
                        char[i] = 1
                    else:
                        char[i] += 1
    return max(char, key=char.get)
