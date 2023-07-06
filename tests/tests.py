'''
test module for translator.py

Author: Thomas Tarango
Date: July 5th, 2023
'''

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from translator import english_to_french, french_to_english


def test_english_to_french():
    print('Testing English to French')
    #first test case, single word translation
    result = english_to_french('Hello')
    assert result, 'Bonjour'

    #second test case, multi word translation
    result = englishToFrench('apple apple')
    assert result == 'matecat matecat'

    #third test case
    result = english_to_french('Hello')
    assert result != 'Hello'
    print('English to French passed all unit tests!')


def test_french_to_english():
    print('Testing French to English')
    #first test case, single word translation
    result = french_to_english('Bonjour')
    assert result == 'Hi'

    #second test case, multi word translation
    result = french_to_english('matecat matecat')
    assert result == 'apple apple'

    #third test case
    result = french_to_english('Bonjour')
    assert result != 'Bonjour'
    print('French to English passed all unit tests!')


if __name__ == '__main__':
    test_english_to_french()
    test_french_to_english()
    