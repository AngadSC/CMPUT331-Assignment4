#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Angad Chahil>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 1 Student Solution
September 2026
Author: Angad Chahil
"""


from sys import flags

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_map(letters=LETTERS):
    char_to_index = {c: i for i, c in enumerate(letters)}
    index_to_char = {i: c for i, c in enumerate(letters)}
    return char_to_index, index_to_char
# builds the the look up tables just walking throuhg them 

def encrypt(message: str, key: str):
    message = message.upper() 
    shift = SHIFTDICT[key.upper()]  # converts the key into the shift 
    translated = ''
    for symbol in message:
        if symbol in SHIFTDICT: # shifts the messahge 
            translated += LETTERDICT[(SHIFTDICT[symbol] + shift) % 26]
        else:
            translated += symbol # maitains symbols and spaces 
    return translated
# adapted from textbook Caesarcipher.py, 

def decrypt(message: str, key: str):
     message = message.upper()
     shift = SHIFTDICT[key.upper()]
     translated = ''
     for symbol in message:
        if symbol in SHIFTDICT:
            translated += LETTERDICT[(SHIFTDICT[symbol] - shift) % 26]
        else:
            translated += symbol
     return translated
# reversed the enccyrpt backward by using key amount 

def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    assert decrypt(encrypt("FOO", "G"), "G") == "FOO"


if __name__ == "__main__" and not flags.interactive:
    test()